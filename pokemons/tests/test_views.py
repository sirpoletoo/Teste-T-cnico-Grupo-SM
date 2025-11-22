from rest_framework.test import APITestCase
from unittest.mock import patch, MagicMock
from pokemons.models import Pokemon
import requests


class PokemonAPITest(APITestCase):
    def setUp(self):
        pass
    
    # mock de criação com PokeAPI
    @patch('pokemons.services.requests.get')
    def test_cria_pokemon_com_pokeapi_sucesso(self, mock_get):
        """Teste se o POST busca dados na POKEAPI e salva."""

        # mock da resposta da pokeapi
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'sprites': {'front_default': 'http://pokeapi.co/bulba.png'},
            'height': 7, # 0.7m
            'weight': 69 # 6.9kg
        }
        mock_get.return_value = mock_response

        # Executa o post
        url = '/api/pokemons/'
        data = {'nome': 'bulbasaur'}
        response = self.client.post(url, data, format='json')

        # verificações
        self.assertEqual(response.status_code, 201) # criado com sucesso
        self.assertEqual(Pokemon.objects.count(), 1)

        # verifica se os dados foram salvos
        pokemon = Pokemon.objects.get(nome='bulbasaur')
        self.assertEqual(pokemon.altura, 7)
        self.assertEqual(pokemon.foto, 'http://pokeapi.co/bulba.png')

        # verifica se o requests.get foi chamado com a url correta
        mock_get.assert_called_once_with('https://pokeapi.co/api/v2/pokemon/bulbasaur/', timeout=10)

    # teste de pokémon não encontrado - 404
    @patch('pokemons.services.requests.get')
    def test_cria_pokemon_invalido_retorna_erro_400(self, mock_get):
        """Testa se Pokémon não encontrado na API retorna 400."""
        
        # mockar a Resposta 404
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
            '404 Client Error: Not Found for url: ...', 
            response=mock_response
        )
        mock_get.return_value = mock_response
        
        # Executar o POST
        url = '/api/pokemons/'
        data = {'nome': 'pokemon-inexistente'}
        response = self.client.post(url, data, format='json')

        # Assertions
        self.assertEqual(response.status_code, 400) # Bad Request
        self.assertEqual(Pokemon.objects.count(), 0)
        self.assertIn("não encontrado na PokeAPI", response.data['nome'])
