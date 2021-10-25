from django.core.validators import MinValueValidator
from django.db import models
import os

from mysite.settings import MEDIA_ROOT

# Create your models here.
class UserInfo(models.Model):
    id = models.AutoField(primary_key=True) # ID
    name = models.CharField(max_length=255) # username
    level = models.IntegerField()
    avatar = models.ImageField(upload_to = 'avatars/', max_length=1000) # path name where the avatar image file is stored
    dob = models.DateField()

    def __str__(self) -> str:
        return self.name


class Manufacturer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Vehicle(models.Model):
    LIGHT_TANK = 'LT'
    MEDIUM_TANK = 'MT'
    HEAVEY_TANK = 'HT'
    TANK_DESTROYER = 'TD'
    ARTELLERY = 'SPG'

    TYPES = (
        (LIGHT_TANK, 'light tank'),
        (MEDIUM_TANK, 'medium tank'),
        (HEAVEY_TANK, 'heavy tank'),
        (TANK_DESTROYER, 'tank destroyer'),
        (ARTELLERY, 'SPG'),
    )


    id = models.AutoField(primary_key=True)
    type = models.CharField(
        max_length=10,
        choices=TYPES,
        default=MEDIUM_TANK,
        )
    capacity = models.IntegerField(default=-1)

    manufacture = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.type