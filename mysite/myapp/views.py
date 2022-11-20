from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Familiar

def index(request):
    return HttpResponse("Jero lindo")

def familiar_por_id(request, familiar_id):
    familiar = Familiar.objects.get(pk=familiar_id)
    return HttpResponse(f"Familiar: {familiar.apellido}, {familiar.nombre}. nacido el {familiar.fechaNac}")