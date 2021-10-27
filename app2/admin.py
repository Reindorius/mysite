from django.contrib import admin

from app2.models import Player, PlayerData, Role

# Register your models here.
admin.site.register(Player)
admin.site.register(Role)
admin.site.register(PlayerData)