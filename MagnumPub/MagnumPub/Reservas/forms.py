from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm


class Formulario_reserva (forms.ModelForm):
    class Meta:
        model=Usuario
        fields=('__all__')
        widgets={
            'Nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Ej:Ingrese nombre de quien reserva'}),
            'Mail':forms.TextInput(attrs={'class':'form-control','placeholder':'Ej: Ingrese mail de quien reserva'}),
            'Teléfono':forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese teléfono de quien reserva'}),
            'Cantidad de personas':forms.TextInput (attrs={'class':'form-control','placeholder':'Cuantas personas?'})
            
        }


