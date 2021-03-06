"""gtfs_farroupilha_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from django.conf.urls.static import static

urlpatterns = [
    
    path('', include('apps.gtfs.urls'), name='gtfs'),

    path('routes/', include('apps.routes.urls'), name='routes'),
    path('trips/', include('apps.trips.urls'), name='trips'),
    path('stops/', include('apps.stops.urls'), name='stops'),
    path('shapes/', include('apps.shapes.urls'), name='shapes'),
    path('stop_times/', include('apps.stop_times.urls'), name='stop_times'),

    path('admin/', admin.site.urls),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
