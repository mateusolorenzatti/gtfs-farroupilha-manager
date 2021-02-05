from django.urls import path

from .views import *

app_name = 'routes'
urlpatterns = [
    path('', index, name='index'),
    path('new', new_route, name='new_route'),
    path('<int:route_id>', show_route, name='show_route'),
    path('<int:route_id>/edit', edit_route, name='edit_route'),
]