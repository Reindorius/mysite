from django.contrib import admin
from .models import Manufacturer, UserInfo, Vehicle
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(Manufacturer)
admin.site.register(Vehicle)