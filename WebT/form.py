from django import forms
from .models import Sensor


class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ('name', 'description', 'ip_address', 'port', 'place', 'max_temperature', 'min_temperature')