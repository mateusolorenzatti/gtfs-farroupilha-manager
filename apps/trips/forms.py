from django import forms
from django.forms import ModelForm

from apps.trips.models import Trips

class GPS_file_form(forms.Form):
    file = forms.FileField(label='Selecione o arquivo do GPS')

class TripForm(forms.ModelForm):
    class Meta:
        model = Trips
        fields = [
            'route',
            'service_id',
            'trip_id', 
            'trip_short_name', 
            'trip_headsign',
            'shape_id',
        ]   
