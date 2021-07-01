from django.contrib import admin
from .models import Sensor
from .models import TData
# Register your models here.


class SensorAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip_address', 'port', 'place', 'max_temperature', 'min_temperature', 'in_range')

class TDataAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'amount', 'datetime')


admin.site.register(Sensor, SensorAdmin)
admin.site.register(TData, TDataAdmin)