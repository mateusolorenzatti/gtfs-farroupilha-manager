from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import GPS_file_form, TripForm

from apps.gtfs.helpers.coordinates import shape_midpoint, shape_midpoint_dict
from apps.gtfs.helpers.handle_uploads import handle_uploaded_file
from apps.gtfs.helpers.gps2gtfs.KML_helper import KML

from apps.trips.models import Trips
from apps.routes.models import Routes
from apps.shapes.models import Shapes
from apps.stops.models import Stops
from apps.stop_times.models import StopTimes


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
def new_trip_manual(request, route_id):
    context = {
        'title' : 'Nova Trip - Manual',
    }

    return render(request,'trips/new/new_trip_manual.html', context)

@login_required
def new_trip_file(request, route_id):

    if request.method == 'POST' and ('file' in request.FILES):
        filename = request.FILES.get('file').name

        extensoes_suportadas = ['.kml']
        if any(ext in filename for ext in extensoes_suportadas):

            new_file = handle_uploaded_file(request.FILES.get('file'), request.user)

            context = {}
            if filename.endswith('.kml'):
                context['stop_times'], context['shapes'] = KML(new_file)

            new_trip_id = '{}{}{}'.format('t_', int(Trips.objects.all().order_by('-trip_id')[0].trip_id[2:8]) + 1, '_b_6309_tn_0')
            
            temp_trip = Trips(
                trip_id = new_trip_id,
                service_id = 'c_5988_b_6309_d_31',
                # shape_id = # Definir o ID da Shape gerada
            )
            
            route = Routes.objects.filter(route_id = route_id)

            if route: temp_trip.route = route[0]

            context['trip_form'] = TripForm(instance = temp_trip)
            
            context['midpoint'] = shape_midpoint_dict(context['shapes'])

            context['title'] = 'Nova Trip - Formulário de Validação'

            return render(request,'trips/new/new_trip_scratch.html', context)

        else: 
            messages.error(request, 'Formato de arquivo inválido! Confira a lista com formatos permitidos')


    context = {
        'title' : 'Nova Trip - Arquivo',
        'route_id': route_id
    }

    return render(request,'trips/new/new_trip_file_upload.html', context)
