from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from .verify import campo_vazio

from apps.agency.models import Agency
from apps.routes.models import Routes
from apps.trips.models import Trips
from apps.stops.models import Stops
from apps.stop_times.models import StopTimes
from apps.shapes.models import Shapes

def home(request):

    return render(request,'gtfs/home.html')

def login(request):

    if request.user.id:
        return redirect('dashboard')

    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request,'Os campos email e senha não podem ficar em branco')
            return redirect('login')

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request,'Email ou senha incorretos!')

    return render(request, 'gtfs/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def login_redirect(request):
    return redirect('login')

@login_required
def dashboard(request):

    context = {'count': {}, }

    context['count']['agency'] = Agency.objects.all().count()
    context['count']['routes'] = Routes.objects.all().count()
    context['count']['shapes'] = Shapes.objects.values('shape_id').distinct().count()
    context['count']['stop_times'] = StopTimes.objects.all().count()
    context['count']['stops'] = Stops.objects.all().count()
    context['count']['trips'] = Trips.objects.all().count()

    return render(request,'gtfs/dashboard.html', context)


