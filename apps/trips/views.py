from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from apps.gtfs.helpers.coordinates import shape_midpoint

from apps.trips.models import Trips
from apps.routes.models import Routes
from apps.shapes.models import Shapes
from apps.stops.models import Stops
from apps.stop_times.models import StopTimes

from .forms import GPS_file_form
from .helpers.handle_uploads import handle_uploaded_file
from .helpers.gps2gtfs.KML_helper import KML

@login_required
def show_trip(request, trip_id):

    trip = get_object_or_404(Trips, trip_id=trip_id)
    route = get_object_or_404(Routes, route_id = trip.route_id)
    
    shapes = Shapes.objects.filter(shape_id = trip.shape_id).order_by('shape_pt_sequence')
    midpoint = shape_midpoint(shapes)

    stop_times = StopTimes.objects.filter(trip = trip.trip_id)

    context = {
        'title' : 'Trajeto {}'.format(trip.trip_id[2:8]),
        'trip': trip,
        'route': route,
        'shapes': shapes,
        'stop_times': stop_times,
        'first_stop': stop_times[0],
        'last_stop': stop_times.order_by('-stop_sequence')[0],
        'midpoint': '[ {}, {} ]'.format(midpoint[0], midpoint[1]),
    }

    return render(request,'trips/show/show_trip.html', context)

@login_required
def new_trip_manual(request):
    context = {
        'title' : 'Nova Trip - Manual',
    }

    return render(request,'trips/new/new_trip_manual.html', context)

@login_required
def new_trip_file(request):

    if request.method == 'POST' and ('file' in request.FILES):
        filename = request.FILES.get('file').name

        extensoes_suportadas = ['.kml']
        if any(ext in filename for ext in extensoes_suportadas):

            new_file = handle_uploaded_file(request.FILES.get('file'), request.user)

            if filename.endswith('.kml'):
                stops, shapes = KML(new_file)


            return redirect('dashboard')

        else: 
            messages.error(request, 'Formato de arquivo inválido! Confira a lista com formatos permitidos')


    context = {
        'title' : 'Nova Trip - Arquivo'
    }

    return render(request,'trips/new/new_trip_file_upload.html', context)
