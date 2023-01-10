from django.db import models

#Modelos App

class Usuario (models.Model):
    nombre= models.CharField (max_length=30)
    mail= models.EmailField (max_length=30)
    telefono= models.IntegerField ()
    fecha_solicitud= models.DateField ()
    fecha_reserva= models.DateField()
    cantidad_personas= models.IntegerField ()

    def __str__(self):
        return f'{self.fecha_reserva} - {self.cantidad_personas} - {self.nombre} - {self.telefono}'

class Mesa (models.Model):
    numero_mesa= models.IntegerField()
    cantidad_personas= models.IntegerField()

    def __str__ (self):
        return f' {self.numero_mesa} - {self.cantidad_personas}' #no se si vamos a ocupar este def, pero que quede, despues vemos


