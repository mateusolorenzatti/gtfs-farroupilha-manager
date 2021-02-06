from django.shortcuts import render
from django.shortcuts import get_object_or_404

from apps.stops.models import Stops
from apps.stop_times.models import StopTimes

def show_stop(request, stop_id):

    stop = get_object_or_404(Stops, stop_id=stop_id)
    stop_times = StopTimes.objects.filter(stop = stop.stop_id).order_by('departure_time')

    context = {
        'title' : 'Parada {}'.format(stop_id),
        'stop': stop,
        'stop_times': stop_times,
    }

    return render(request,'stops/show/show_stop.html', context)
