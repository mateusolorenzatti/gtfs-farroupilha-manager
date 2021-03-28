from django.urls import path

from .views import *

app_name = 'shapes'
urlpatterns = [
    path('api/new_list', new_shape_list_api, name='new_shape_list_api'),
]