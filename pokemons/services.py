import requests

class PokeAPIService:
    """
    Responsável por buscar dados na PokeAPI
    """
    BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

    def buscar_dados_pokemon(self, nome_pokemon):
        """
        Faz uma requisição GET para a PokeAPI.
        Retorna foto, altura e peso.
        Devolve uma mensagem de erro caso o Pokemon não seja encontrado
        """

        nome_formatado = nome_pokemon.lower()
        url = f"{self.BASE_URL}{nome_formatado}/"

        try:
            # Fazer a requisição HTTP
            response = requests.get(url, timeout=10)
            response.raise_for_status()

        except requests.exceptions.HTTPError as e:
            # Tratar o erro 404
            if response.status_code == 404:
                # Gera uma exceção personalizada no Serializer
                raise ValueError(f"Pokémon '{nome_pokemon}' não encontrado na PokeAPI")
            
            # Trata os demais erros
            raise ConnectionError(f"Erro ao conectar na PokeAPI: {e}")
        
        except requests.exceptions.RequestException as e:
            # Trata erros de conexão
            raise ConnectionError(f"Erro de rede ao buscar Pokémon: {e}")
        
        data = response.json()

        # Extrair e retornar os dados
        return {
            'foto': data['sprites']['front_default'],
            'altura': data['height'], # CM
            'peso': data['weight'] # HECTOGRAMAS
        }