from rest_framework import serializers
from .models import Treinador, Pokemon

class TreinadorSerializer(serializers.ModelSerializer):
    """
    Responsável pela control dos serialização/desserialização para a API REST. 
    """
    class Meta:
        model = Treinador
        fields = ['id', 'nome', 'idade', 'criado_em', 'atualizado_em']
        read_only_fields = ['id', 'criado_em', 'atualizado_em']




class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['id', 'nome', 'foto', 'altura', 'peso', 'criado_em', 'atualizado_em']
        read_only_fields = ['id', 'nome', 'foto', 'altura', 'peso', 'criado_em', 'atualizado_em']

        extra_kwargs = {
            'nome': {'required': True, 'allow_blank': False}
        }