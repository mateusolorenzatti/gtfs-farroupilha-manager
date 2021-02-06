from django.urls import path

from .views import *

app_name = 'stops'
urlpatterns = [
    # path('', index, name='index'),
    path('<str:stop_id>', show_stop, name='show_stop'),
    # path('<int:route_id>/edit', edit_route, name='edit_route'),
]