from django.urls import path

from .views import *

app_name = 'routes'
urlpatterns = [
    path('', index, name='index'),
    path('<int:route_id>', route_detail, name='route_detail'),
]