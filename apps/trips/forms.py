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
            'trip_id', 
            'service_id',
            'trip_short_name', 
            'trip_headsign',
            'shape_id',
        ]
        labels = {
            "route": "Rota",
            "trip_id": "ID do Trajeto (Autogerado)", 
            "service_id": "Serviço (Autogerado)",
            "trip_short_name": "Short Name (Opcional)", 
            "trip_headsign": "Nome no Visor (Opcional)",
            "shape_id": "Shape (Já associada ao Trajeto)",
        }

