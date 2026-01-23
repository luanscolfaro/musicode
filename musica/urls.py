from django.urls import path
from .views import calcular_musica

urlpatterns = [
    path("calcular/", calcular_musica),
]
