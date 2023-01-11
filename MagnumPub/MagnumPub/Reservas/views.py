from http.client import HTTPResponse
from django.shortcuts import render
from django.template import loader
from .forms import UsuarioForm



def inicio (request):
    if request.method == "POST":
        form=UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error",form.errors)
    form=UsuarioForm()    
    return render (request,"inicio.html",{'form':form})

