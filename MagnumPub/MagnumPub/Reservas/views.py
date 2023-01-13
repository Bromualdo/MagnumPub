from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.template import loader
from .forms import UsuarioForm
from .models import Usuario
from datetime import datetime, time


def inicio (request):
    hora_limite=time (20,30,00)
    hora_limite_str=hora_limite.strftime ("%H:%M:%S")
    hora_inicio=time (8,00,00)
    hora_inicio_str=hora_inicio.strftime ("%H:%M:%S")
    hora_actual=datetime.now ()
    hora_actual_str=hora_actual.strftime("%H:%M:%S")
    if hora_actual_str < hora_limite_str and hora_actual_str > hora_inicio_str:
        if request.method == "POST":
            form=UsuarioForm(request.POST)
            if form.is_valid():
                fecha=form.cleaned_data["fecha_reserva"]
            # formato=fecha.strftime("%d/%m/%y")
            
                if Usuario.objects.filter(fecha_reserva__icontains=fecha).count() >= 9:
                               
                    return redirect ("limite")
                else:
                    form.save()
           
                    return redirect ("confirmacion")

            else:
                print("Error",form.errors)
        form=UsuarioForm()    
        return render (request,"inicio.html",{'form':form})
    else:
        return render (request, "fuera_horario.html")
def confirmacion (request):
    return render (request, "confirmacion.html")

def limite (request):
    return render (request, "limite.html")

def vista (request):   
    lista = Usuario.objects.all().order_by('fecha_reserva') 
    return render(request, "vista.html",{"reserva": lista} )

def eliminar_reserva(request,id):
    
    if request.method == "POST":
        
        eliminar= Usuario.objects.get(id=id)
        eliminar.delete()        
       
        
        return render(request, "vista.html", {'eliminar': eliminar})    