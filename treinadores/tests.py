from rest_framework.test import APITestCase
from treinadores.models import Treinador
from pokemons.models import Pokemon
from rest_framework import status

class TreinadorRelacionamentoTest(APITestCase):
    def setUp(self):
        # cria um treinador e um pokémon pra usar nos testes
        self.treinador = Treinador.objects.create(nome='Ash Ketchum', idade=10)
        self.pikachu = Pokemon.objects.create(nome='Pikachu', peso=60, altura=4)
        self.squirtle = Pokemon.objects.create(nome='Squirtle', peso=90, altura=5)
        
        self.adicionar_url = f'/api/treinadores/{self.treinador.id}/adicionar_pokemon/'
        self.remover_url = f'/api/treinadores/{self.treinador.id}/remover_pokemon/'
        
    # teste de adicionar um pokémon
    
    def test_adicionar_pokemon_com_sucesso(self):
        # testa se um pokemon é adicionado ao treiandor
        payload = {'pokemon_id': self.pikachu.id}
        # executa o post
        response = self.client.post(self.adicionar_url, payload, format='json')
        # checa se deu sucesso (200 ok)
        self.assertEqual(response.status_code, 200)
        # verifica se foi salvo no banco
        self.assertIn(self.pikachu, self.treinador.pokemons.all())
        
    def test_adicionar_pokemon_inexistente(self):
        #testa se retorna 404 ao tentar adicionar pokémon que não existe
        payload = {'pokemon_id': '4999'} # id inexistente
        response = self.client.post(self.adicionar_url, payload, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
     
     # teste de remover um pokémon
    def test_remover_pokemon_com_sucesso(self):
         # testa remover um pokémon que pertence a um treinador
         self.treinador.pokemons.add(self.squirtle)
         
         # confirma se tem o pokémon antes do teste
         self.assertIn(self.squirtle, self.treinador.pokemons.all())
         
         # executa a remoção
         payload = {'pokemon_id': self.squirtle.id}
         response = self.client.post(self.remover_url, payload, format='json')
         
         #verifica o status e se foi removido do banco
         self.assertEqual(response.status_code, 200)
         self.assertNotIn(self.squirtle, self.treinador.pokemons.all()) # NotIn verifica se foi removido de fato
