from django.urls import path
from .views import inicio,formulario_reserva
from .models import Usuario

urlpatterns = [
    path("", inicio, name ='inicio'),
    path ("", formulario_reserva,name='Reserva'),
            ]