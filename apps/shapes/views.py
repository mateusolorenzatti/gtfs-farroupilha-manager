import json

from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from apps.shapes.models import Shapes

@ensure_csrf_cookie
def new_shape_list_api(request):
    if not request.user.username:
        return JsonResponse({'Erro': 'Não autorizado' }, status=403)

    if request.method == 'POST':
        shapes_json = request.POST.get('shapes')

        shapes = json.loads(shapes_json)

        """
        for shape in shapes:
            Shapes(
               shape_pt_lon = shape['shape_pt_lon'],
               shape_pt_lat = shape['shape_pt_lat'],
               shape_pt_sequence = shape['shape_pt_sequence'],
               shape_id = shape['shape_id']
            ).save()
        """
        
        return JsonResponse({
            'Sucesso': 'Shapes criadas com sucesso!'
        })

    return JsonResponse({ 'Erro': 'Aceitamos apenas POST' })