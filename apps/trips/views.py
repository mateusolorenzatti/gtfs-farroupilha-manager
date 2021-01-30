from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.db.models import Q

from apps.gtfs.helpers.coordinates import shape_midpoint

from apps.trips.models import Trips
from apps.routes.models import Routes
from apps.shapes.models import Shapes
from apps.stops.models import Stops
from apps.stop_times.models import StopTimes

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
        'midpoint': '[ {}, {} ]'.format(midpoint[0], midpoint[1]),
    }

    return render(request,'trips/show/show_trip.html', context)
