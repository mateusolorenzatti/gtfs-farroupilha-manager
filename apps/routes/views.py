from django.shortcuts import render
from  django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import get_object_or_404

import unidecode

from apps.routes.models import Routes
from apps.trips.models import Trips

ROUTES_PER_PAGE = 15

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
        'routes' : rotas_pag,
        'query': query
    }

    return render(request,'routes/routes.html', context)

def route_detail(request, route_id):
    route = get_object_or_404(Routes, route_id=route_id)

    trips = Trips.objects.all().filter(route = route_id)

    context = {
        'title' : 'Rota {}'.format(route.route_id),
        'route' : route,
        'trips': trips
    }

    return render(request,'routes/detail/route_detail.html', context)