from django.shortcuts import render

from rest_framework import viewsets
from .models import Treinador, Pokemon
from .serializers import TreinadorSerializer, PokemonSerializer

"""
Viewset é como se fosse o Controller, vai gerenciar as operações CRUD

"""
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer