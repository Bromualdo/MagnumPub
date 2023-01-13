from django.urls import path
from .views import inicio,vista,eliminar_reserva, confirmacion,limite,login_usuario

from django.views.i18n import JavaScriptCatalog



urlpatterns = [
    path("", inicio, name ='inicio'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
    path ("confirmacion", confirmacion, name="confirmacion"),
    path ("limite", limite, name="limite"),
    path("vista", vista, name ='vista'),
    path('eliminar/<int:id>',eliminar_reserva,name='eliminar_reserva'),
    path ("login_usuario/", login_usuario, name ="Login"),

            ]