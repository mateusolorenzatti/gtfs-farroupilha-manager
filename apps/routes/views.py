from django.shortcuts import render
from  django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

import unidecode

from apps.routes.models import Routes

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
        'routes' : rotas_pag,
        'query': query
    }

    return render(request,'routes/routes.html', context)