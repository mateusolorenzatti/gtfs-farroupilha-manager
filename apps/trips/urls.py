from django.urls import path

from .views import *

app_name = 'trips'
urlpatterns = [
    path('detail/<str:trip_id>/', show_trip, name='show_trip'),
    path('new_manual/', new_trip_manual, name='new_trip_manual'),
    path('new_file/', new_trip_file, name='new_trip_file'),
]