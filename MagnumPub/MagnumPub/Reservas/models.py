from django.db import models
from datetime import datetime, date
from django.contrib.admin.widgets import AdminDateWidget,AdminTimeWidget,AdminSplitDateTime

#Modelos App

class Usuario (models.Model):
    nombre= models.CharField (max_length=30, null=True)
    mail= models.EmailField (max_length=30)
    telefono= models.IntegerField ()
    fecha_reserva= models.DateField(auto_now_add=False , auto_now= False , blank=True , null=True)
    cantidad_personas= models.IntegerField ()
    
    
    def __str__ (self):
         return f'{self.nombre} - {self.mail} - {self.telefono} - {self.fecha_reserva} - {self.cantidad_personas}'

    

class Mesa (models.Model):
    numero_mesa= models.IntegerField()
    cantidad_personas= models.IntegerField()

    def __str__ (self):
        return f' {self.numero_mesa} - {self.cantidad_personas}' #sin uso


