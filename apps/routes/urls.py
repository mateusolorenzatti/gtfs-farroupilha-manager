from django.urls import path

from .views import *

app_name = 'routes'
urlpatterns = [
    path('', index, name='index'),
]