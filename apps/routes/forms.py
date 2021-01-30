from django.db import models
from django.forms import ModelForm

from apps.routes.models import Routes

class RoutesForm(ModelForm):
    class Meta:
        model = Routes
        fields = [
            'route_id', 
            'route_short_name', 
            'route_long_name',
            'route_type',
            'route_color'
        ]

        # widgets = {
        #     'route_id': Textarea(attrs={'': 80, 'rows': 20}),
        # }
