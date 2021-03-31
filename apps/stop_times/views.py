import json

from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from apps.stop_times.models import StopTimes
from apps.stops.models import Stops
from apps.trips.models import Trips

@ensure_csrf_cookie
def new_stop_time_list_api(request):

    if not request.user.username:
        return JsonResponse({'Erro': 'Não autorizado' }, status=403)

    if request.method == 'POST':
        st_json = request.POST.get('stop_times')

        stop_times = json.loads(st_json)
        trip = Trips.objects.get(trip_id = stop_times[0]['trip_id'])

        for stop_time in stop_times:
            stop = Stops.objects.get(stop_id = int(stop_time['stop_id']))
            
            StopTimes(
               trip = trip,
               stop = stop,
               arrival_time = stop_time['arrival_time'],
               departure_time = stop_time['arrival_time'],
               stop_sequence = stop_time['stop_sequence']
            ).save()
                
        return JsonResponse({
            'Sucesso': 'Stop Times criadas com sucesso!'
        })

    return JsonResponse({ 'Erro': 'Aceitamos apenas POST' })