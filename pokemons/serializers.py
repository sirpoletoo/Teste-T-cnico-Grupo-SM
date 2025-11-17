from rest_framework import serializers
from .models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['id', 'nome', 'foto', 'altura', 'peso', 'criado_em', 'atualizado_em']
        read_only_fields = ['id', 'nome', 'foto', 'altura', 'peso', 'criado_em', 'atualizado_em']

        extra_kwargs = {
            'nome': {'required': True, 'allow_blank': False}
        }