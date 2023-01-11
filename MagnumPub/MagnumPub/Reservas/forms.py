from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget,AdminTimeWidget,AdminSplitDateTime

   
class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model =Usuario
        fields="__all__"
        widgets ={"fecha_reserva":AdminDateWidget(),
                  "hora":AdminTimeWidget()                  
                  }
        
