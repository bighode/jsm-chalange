from django.urls import path
from . import views

urlpatterns = [
    path('', views.getHome),
    path('clientes', views.getClientes),
]