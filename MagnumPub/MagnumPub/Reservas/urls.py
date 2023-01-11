from django.urls import path
from .views import inicio

from django.views.i18n import JavaScriptCatalog



urlpatterns = [
    path("", inicio, name ='inicio'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),

            ]