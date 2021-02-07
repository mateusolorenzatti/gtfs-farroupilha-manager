from django.db import models
from django.forms import ModelForm, FloatField

from apps.stops.models import Stops

class StopsForm(ModelForm):
    class Meta:
        model = Stops
        fields = [
            'stop_lat',
            'stop_lon',
            'stop_id', 
            'stop_name', 
            'stop_timezone',
        ]   