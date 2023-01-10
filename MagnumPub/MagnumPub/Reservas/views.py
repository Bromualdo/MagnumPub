from http.client import HTTPResponse
from django.shortcuts import render
from django.template import loader
from .forms import Formulario_reserva
from .models import Usuario

def inicio (request):
    
    return render (request,"inicio.html")


def formulario_reserva (request):
    if request.method == "POST":
        mi_formulario = Formulario_reserva (request.POST)
        if mi_formulario.is_valid():
            data= mi_formulario.cleaned_data
            formulario = Usuario (nombre=data ['nombre'], Mail= data ['mail'], telefono= data ['telefono'],fecha_solicitud=data['fecha_solicitud'],fecha_reserva=data['fecha_reserva'],cantidad_personas=['cantidad_personas'])
            formulario.save()



            # return redirect ("agregado")
    else:
            mi_formulario = Formulario_reserva ()
    return render (request, "inicio.html", {'mi_formulario': mi_formulario})