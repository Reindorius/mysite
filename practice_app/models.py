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