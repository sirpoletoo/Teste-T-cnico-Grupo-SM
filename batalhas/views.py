from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from pokemons.models import Pokemon

class BatalhaView(APIView):
    """
    API para simular uma batalha entre dois pokémons.
    Ganha o pokémon que tiver o maior peso
    Peso igual resulta em empate
    Dois pokémons do mesmo treinador não podem lutar entre si
    POST /api/batalhar
    """

    def post(self, request):
        pokemon_id_1 = request.data.get('pokemon1_id')
        pokemon_id_2 = request.data.get('pokemon2_id')
        if not pokemon_id_1 or not pokemon_id_2:
            return Response(
                {"erro": "É necessário informar 'pokemon1_id' e 'pokemon2_id'"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        # Buscar os objetos no anco. get_object_or_404 retorna um 404 se não existir
        p1 = get_object_or_404(Pokemon, pk=pokemon_id_1)
        p2 = get_object_or_404(Pokemon, pk=pokemon_id_2)

        # Busca os IDs de treinadores para cada Pokémon
        treinadores_p1 = set(p1.treinadores.values_list('id', flat=True))
        treinadores_p2 = set(p2.treinadores.values_list('id', flat=True))

        if not treinadores_p1.isdisjoint(treinadores_p2):
            return Response(
                {"erro": "Batalha cancelada: Os Pokémons pertencem ao mesmo treinador"},
                status=status.HTTP_400_BAD_REQUEST
            )
        # Regra de negócio: Ganha o Pokémon que tiver o maior peso
        vencedor = None
        mensagem = "Empate! (Mesmo peso)"

        if p1.peso > p2.peso:
            vencedor = p1.nome
            mensagem = f"{p1.nome} venceu {p2.nome} nesse duelo eletrizante!"
        elif p2.peso > p1.peso:
            vencedor = p2.nome
            mensagem = f"{p2.nome} venceu {p1.nome} nesse duelo incrível!"
        
        return Response({
            "pokemon_1": {"nome": p1.nome, "peso": f"{p1.peso}hg"},
            "pokemon_2": {"nome": p2.nome, "peso": f"{p2.peso}hg"},
            "resultado": mensagem, 
            "vencedor": vencedor
        }, status=status.HTTP_200_OK)