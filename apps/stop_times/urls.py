from django.urls import path

from .views import *

app_name = 'stop_times'
urlpatterns = [
    path('api/new_list', new_stop_time_list_api, name='new_stop_time_list_api'),
]