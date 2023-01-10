from http.client import HTTPResponse
from django.shortcuts import render
from django.template import loader


def inicio (request):
    return render (request,"inicio.html")
