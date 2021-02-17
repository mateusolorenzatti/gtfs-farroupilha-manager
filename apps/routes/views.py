from django.shortcuts import render, redirect
from  django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

import unidecode

from apps.routes.forms import RoutesForm

from apps.routes.models import Routes
from apps.trips.models import Trips

ROUTES_PER_PAGE = 15

@login_required
def index(request):
    rotas = Routes.objects.order_by('route_long_name')
    query = request.GET.get('q')
    
    if query:
        query_unicode = unidecode.unidecode(query)

        rotas = rotas.filter(
            Q(route_long_name__icontains=query) | Q(route_long_name__icontains=query_unicode)
        )
    
    paginator = Paginator(rotas, ROUTES_PER_PAGE)
    page = request.GET.get('page')
    rotas_pag = paginator.get_page(page)

    context = {
        'title' : 'Rotas',
        'prev_url': 'dashboard',
        'routes' : rotas_pag,
        'query': query
    }

    return render(request,'routes/routes.html', context)

@login_required
def show_route(request, route_id):
    route = get_object_or_404(Routes, route_id=route_id)

    trips = Trips.objects.all().filter(route = route_id)

    context = {
        'title' : 'Rota {}'.format(route.route_id),
        'prev_url': 'routes:index',
        'route' : route,
        'trips': trips
    }

    return render(request,'routes/show/show_route.html', context)

@login_required
def new_route(request):

    if request.method == 'POST':
        form = RoutesForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Rota criada com sucesso!')

            return redirect('routes:show_route', form.cleaned_data['route_id'])

        else:
            messages.error(request,'Ocorreu um erro ao criar a Rota')
            form = RoutesForm()
    else:
        form = RoutesForm()

    context = {
        'title' : 'Criar uma Rota',
        'form': form
    }

    return render(request,'routes/new/new_route.html', context)

@login_required
def edit_route(request, route_id):
    route = get_object_or_404(Routes, route_id=route_id)

    if request.method == 'POST':
        form = RoutesForm(request.POST, instance = route)

        if form.is_valid():
            form.save()
            messages.success(request,'Rota alterada com sucesso!')

            return redirect('routes:show_route', route_id)
        else:
            form = RoutesForm(instance = route)
    else:
        form = RoutesForm(instance = route)

    context = {
        'title' : 'Editar a Rota {}'.format(route.route_id),
        'form': form,
        'route' : route,
    }

    return render(request,'routes/edit/edit_route.html', context)