from django.urls import path

from .views import *

app_name = 'trips'
urlpatterns = [
    path('detail/<str:trip_id>/', show_trip, name='show_trip'),
    path('new_manual/<int:route_id>', new_trip_manual, name='new_trip_manual'),
    path('new_file/<int:route_id>', new_trip_file, name='new_trip_file'),
]