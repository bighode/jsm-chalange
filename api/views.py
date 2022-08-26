from django.shortcuts import render
from rest_framework import viewsets

from . models import Cliente
from . serializer import ClienteSerializer

class ClienteView(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer