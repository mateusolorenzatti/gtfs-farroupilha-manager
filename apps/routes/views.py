from django.shortcuts import render
from  django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from apps.routes.models import Routes

ROUTES_PER_PAGE = 15

def index(request):
    rotas = Routes.objects.order_by('route_long_name')

    paginator = Paginator(rotas, ROUTES_PER_PAGE)
    page = request.GET.get('page')
    rotas_pag = paginator.get_page(page)

    context = {
        'routes' : rotas_pag
    }

    return render(request,'routes/routes.html', context)