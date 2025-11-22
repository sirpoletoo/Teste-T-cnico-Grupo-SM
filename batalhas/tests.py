from rest_framework.test import APITestCase
from pokemons.models import Pokemon
from treinadores.models import Treinador

class BatalhaAPITest(APITestCase):
    def setUp(self):
        # cria treinadores
        self.ash = Treinador.objects.create(nome='Ash', idade=10)
        self.misty = Treinador.objects.create(nome='Misty', idade=10)
        
        # cria pokémons
        self.pokemon_pesado = Pokemon.objects.create(nome='Snorlax', peso=4600, altura=21)
        self.pokemon_leve = Pokemon.objects.create(nome='Jigglypuff', peso=55, altura=5)
        self.pokemon_empate = Pokemon.objects.create(nome='Ditto', peso=40, altura=3)
        self.pokemon_p3 = Pokemon.objects.create(nome='Mew', peso=40, altura=4)
        
        # define qual treinador tem qual pokemon
        self.ash.pokemons.add(self.pokemon_pesado, self.pokemon_empate)
        self.misty.pokemons.add(self.pokemon_leve, self.pokemon_p3)
        
        self.url = '/api/batalhar/'
        
    def test_vitoria_por_peso(self):
        # teste se o pokémon mais pesado vence a batalha
        data = {
            "pokemon1_id": self.pokemon_pesado.pk, 
            "pokemon2_id": self.pokemon_leve.pk
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['vencedor'], 'Snorlax')
            
    def test_empate_por_peso(self):
        """Testa se a batalha resulta em empate quando os pesos são iguais."""
        data = {
            "pokemon1_id": self.pokemon_empate.pk, # 40
            "pokemon2_id": self.pokemon_p3.pk      # 40
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['vencedor'], None)
        self.assertIn('Empate!', response.data['resultado'])