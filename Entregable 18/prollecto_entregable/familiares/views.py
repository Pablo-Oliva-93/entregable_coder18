from django.shortcuts import render
from django.http import HttpResponse

from familiares.models import Familiar

# Create your views here.
def crear_familiar(request):
    familiar = Familiar.objects.create(nombre="Sergio", altura=1.73, casado=False, edad=30)
    return HttpResponse("Nuevo familiar creado")

def ver_familiares(request):
    lista_familiares = Familiar.objects.all()
    context = {
        "familires": lista_familiares,
    }
    return render(request, "ver_familiares.html", context=context)