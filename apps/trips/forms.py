from django import forms

class GPS_file_form(forms.Form):
    file = forms.FileField(label='Selecione o arquivo do GPS')