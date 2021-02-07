from django.urls import path

from .views import *

app_name = 'stops'
urlpatterns = [
    path('', index, name='index'),
    path('<int:stop_id>', show_stop, name='show_stop'),
    path('new', new_stop, name='new_stop'),
    path('delete/<int:stop_id>', delete_stop, name='delete_stop'),
    # path('<int:route_id>/edit', edit_route, name='edit_route'),
]