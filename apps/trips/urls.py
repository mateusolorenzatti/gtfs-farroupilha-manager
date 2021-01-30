from django.urls import path

from .views import *

app_name = 'trips'
urlpatterns = [
    # path('', index, name='index'),
    path('<str:trip_id>', show_trip, name='show_trip'),
    # path('<int:route_id>/edit', edit_route, name='edit_route'),
]