from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.template import loader
from .forms import UsuarioForm
from .models import Usuario
import datetime


def inicio (request):
    
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

def confirmacion (request):
    return render (request, "confirmacion.html")

def limite (request):
    return render (request, "limite.html")

def vista (request):   
    lista = Usuario.objects.all()    
    return render(request, "vista.html",{"reserva": lista} )

def eliminar_reserva(request,id):
    
    if request.method == "POST":
        
        eliminar= Usuario.objects.get(id=id)
        eliminar.delete()        
       
        
        return render(request, "vista.html", {'eliminar': eliminar})    