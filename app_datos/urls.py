from django.urls import path
#IMPORTAR LAS VIEWS
from . import views

urlpatterns = [
    path("", views.inicio),
    path("registro", views.registro),
    path("busqueda_datos", views.busqueda_datos),
    path("buscar", views.buscar),
]
