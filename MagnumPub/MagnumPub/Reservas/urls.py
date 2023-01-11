from django.urls import path
from .views import inicio,vista,eliminar_reserva

from django.views.i18n import JavaScriptCatalog



urlpatterns = [
    path("", inicio, name ='inicio'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
    path("vista", vista, name ='vista'),
    path('eliminar/<int:id>',eliminar_reserva,name='eliminar_reserva'),

            ]