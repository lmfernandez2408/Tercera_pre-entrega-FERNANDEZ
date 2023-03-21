"""
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""
from django.urls import path
from app_morrison import views

urlpatterns = [
    path("", views.index, name="index"),
    path('inicio/', views.Inicio, name="inicio"),
    path("Clientes/", views.Clientes, name="Clientes"),
    path("Pedidos/", views.Pedidos, name="Pedidos"),
    path("Personal/", views.Personal, name="Personal"),
]