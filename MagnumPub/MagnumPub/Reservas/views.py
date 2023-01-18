from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.template import loader
from .forms import UsuarioForm
from .models import Usuario
from datetime import datetime, time
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.views import LogoutView

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
                formato=fecha.strftime("%A/%m/%y")
                if formato[:6] == 'Monday':
                    return redirect ("lunes")
                    # form.cleaned_data["fecha_reserva"]=formato
                
                
                else:
                    if Usuario.objects.filter(fecha_reserva__icontains=fecha).count() >=10:
                         
                        return redirect ("limite")
                    else:
                    
                        form.save()
           
                    return redirect ("confirmacion")

            else:
                return redirect ("error")
        form=UsuarioForm()    
        return render (request,"inicio.html",{'form':form})
    else:
        return render (request, "fuera_horario.html")

def confirmacion (request):
    return render (request, "confirmacion.html")

def fuera_horario (request):
    return render (request, "fuera_horario.html")

def limite (request):
    return render (request, "limite.html")

def error (request):
    return render (request, "error.html")

def lunes (request):
    return render (request, "lunes.html")



@permission_required('Reservas.delete_usuario', raise_exception=True)
@login_required(login_url='inicio')  
def vista (request):   
    lista = Usuario.objects.all().order_by('fecha_reserva') 
    return render(request, "vista.html",{"reserva": lista} )

@permission_required('Reservas.delete_usuario', raise_exception=True)
@login_required(login_url='inicio')  
def eliminar_reserva(request,id):
    
    if request.method == "POST":
        
        eliminar= Usuario.objects.get(id=id)
        eliminar.delete()        
       
        
    return redirect("vista")
    


def login_usuario (request):

    if request.method == 'POST':

        formulario_login_usuario = AuthenticationForm(request, data=request.POST)

        if formulario_login_usuario.is_valid():

            data = formulario_login_usuario.cleaned_data

            nombre_usuario = data["username"]
            password_usuario = data["password"]

            user = authenticate(username=nombre_usuario, password=password_usuario)

            if user:

                login(request, user)
                
                return render (request, "inicio_login.html", {"mensaje": f'Bienvenido {nombre_usuario}'})
        
        return render(request, "error_login.html", {"mensaje": f'Error en la carga de datos'})
    
    else:

        formulario_login_usuario = AuthenticationForm()

        return render(request, "login.html", {"formulario_login": formulario_login_usuario})
