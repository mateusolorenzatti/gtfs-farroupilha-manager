from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse, JsonResponse
from django.core import serializers

import json
import unidecode

from apps.stops.models import Stops
from apps.stop_times.models import StopTimes

from apps.stops.forms import StopsForm

STOPS_PER_PAGE = 15

@login_required
def index(request):
    stops = Stops.objects.order_by('stop_name')
    query = request.GET.get('q')
    
    if query:
        query_unicode = unidecode.unidecode(query)

        stops = stops.filter(
            Q(stop_name__icontains=query) | Q(stop_name__icontains=query_unicode)
        )
    
    paginator = Paginator(stops, STOPS_PER_PAGE)
    page = request.GET.get('page')
    stops_pag = paginator.get_page(page)

    index = stops_pag.number - 1 
    max_index = len(paginator.page_range)

    start_index = index - 4 if index >= 4 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index

    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'title' : 'Paradas',
        'prev_url': 'dashboard',
        'stops' : stops_pag,
        'page_range' : page_range,
        'query': query
    }

    return render(request,'stops/index/stops.html', context)

@login_required
def new_stop(request):

    if request.method == 'POST':
        form = StopsForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Parada criada com sucesso!')

            return redirect('stops:show_stop', form.cleaned_data['stop_id'])        
        else:
            messages.error(request,'Ocorreu um erro ao criar a Parada')

            print(form.errors)

    last_stops = Stops.objects.all().order_by('-stop_id')[0]
    stop_modelo = Stops(stop_id = last_stops.stop_id + 1, stop_timezone='America/Sao_Paulo', stop_lon=-51.348123, stop_lat=-29.226622)

    form = StopsForm(instance = stop_modelo)

    context = {
        'title' : 'Criar uma Parada',
        'form': form
    }

    return render(request,'stops/new/new_stop.html', context)

@login_required
def show_stop(request, stop_id):

    stop = get_object_or_404(Stops, stop_id=stop_id)
    stop_times = StopTimes.objects.filter(stop = stop.stop_id).order_by('departure_time')

    context = {
        'title' : 'Parada {}'.format(stop_id),
        'prev_url': 'stops:index',
        'stop': stop,
        'stop_times': stop_times,
    }

    return render(request,'stops/show/show_stop.html', context)

@login_required
def edit_stop(request, stop_id):
    stop = get_object_or_404(Stops, stop_id=stop_id)

    if request.method == 'POST':
        form = StopsForm(request.POST, instance = stop)

        if form.is_valid():
            form.save()
            messages.success(request,'Parada alterada com sucesso!')

            return redirect('stops:show_stop', stop_id)
        else:
            form = StopsForm(instance = stop)
    else:
        form = StopsForm(instance = stop)

    context = {
        'title' : 'Editar a Parada {}'.format(stop_id),
        'form': form,
        'stop' : stop,
    }

    return render(request,'stops/edit/edit_stop.html', context)

@login_required
def delete_stop(request, stop_id):
    instance = Stops.objects.get(stop_id = stop_id)

    if (instance is not None):
        instance.delete()
        messages.success(request, "Parada {} excluída com sucesso! ".format(stop_id))
    else:
        messages.error(request, "Parada inexistente! ".format(stop_id))

    return redirect('stops:index')     

@ensure_csrf_cookie
def new_stop_api(request):
    if not request.user.username:
        return JsonResponse({'Erro': 'Não autorizado' }, status=403)

    if request.method == 'POST':

        last_stop = Stops.objects.all().order_by('-stop_id')[0]
        new_stop = Stops(
            stop_id = last_stop.stop_id + 1, 
            stop_name = request.POST.get('stop_name'),
            stop_timezone = request.POST.get('stop_timezone'), 
            stop_lon = request.POST.get('stop_lon'), 
            stop_lat = request.POST.get('stop_lat')
        )

        new_stop.save(force_insert=True)
        
        return JsonResponse({
            'stop': { 
                'stop_id': new_stop.stop_id,
                'stop_name': new_stop.stop_name
            }
        })

    return JsonResponse({ 'Erro': 'Aceitamos apenas POST' })
