from django.contrib import admin
from .models import Device


# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    list_display = ['device_name', 'device_sys', 'device_version', 'device_brand', 'device_owner', 'create_time']


admin.site.register(Device, DeviceAdmin)
