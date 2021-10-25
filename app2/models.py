from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from django.db import models

class Player(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.TextField(max_length=127, default=id.__str__() + '_first_name')
    lastName = models.TextField(max_length=127, default=id.__str__() + '_last_name')
    level = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.firstName + " " + self.lastName



class Role(models.Model):
    id = models.AutoField(primary_key=True)
    
    class Type(models.TextChoices):
        TANK = 'T',_('Tank')
        HEALER = 'H',_('Healer')
        MELEE = 'M',_('Melee')
        RANGE = 'R',_('Ranger')
        CASTER = 'C',_('Caster')
    
    type = models.CharField(
        max_length=2,
        choices=Type.choices,
        default=Type.MELEE,
    )

    name = models.TextField(max_length=63)



class PlayerData(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    date_updated = models.DateField()