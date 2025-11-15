from rest_framework import serializers
from .models import Treinador

class TreinadorSerializer(serializers.ModelSerializer):
    """
    Responsável pela control dos serialização/desserialização para a API REST. 
    """
    class Meta:
        model = Treinador
        fields = ['id', 'nome', 'idade', 'criado_em', 'atualizado_em']
        read_only_fields = ['id', 'criado_em', 'atualizado_em']