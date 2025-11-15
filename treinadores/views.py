from django.shortcuts import render

from rest_framework import viewsets
from .models import Treinador
from .serializers import TreinadorSerializer

"""
Viewset é como se fosse o Controller, vai gerenciar as operações CRUD

"""
class TreinadorViewSet(viewsets.ModelViewSet):
    # Fornece as operações CRUD
    # Consulta no Repository
    queryset = Treinador.objects.all()

    # Serializer traduz as infos para json
    serializer_class = TreinadorSerializer