# O que é uma API?
Uma API (Application Programming Interface) é um intermediário que permite a dois softwares se comunicarem.

Ela define um conjunto de regras (como URLs, métodos HTTP e formato de dados) que um aplicativo usa para solicitar serviços ou informações de outro.

No desenvolvimento web com Django, a API é o que permite que seu frontend (navegador/app) obtenha e envie dados para o backend (servidor Django).

# o que é esse projeto?
Este projeto é uma API RESTful de Pokédex desenvolvida como um desafio técnico, utilizando Python 3.11+, Django 5+ e Django Rest Framework. A aplicação gerencia o CRUD completo de Treinadores e Pokémons, implementando a relação muitos-para-muitos entre eles. Além disso, inclui a lógica de negócio para simulação de batalhas e integra-se à PokeAPI para enriquecimento de dados. Os dados são persistidos utilizando PostgreSQL.

# Como rodar o Projeto
## 1. Instalar o Python
- Link do Python 3.11: https://www.python.org/downloads/

## 2. Instalar o Django e criando o ambiente virtual
Rodar todos os comandos no terminal
- Criação do ambiente virtual: python -m venv venv
- Ativação do Ambiente Virtual:
macOS/Linux: source venv/bin/activate
Windows (PowerShell): .\venv\Scripts\Activate.ps1
Windows (Cmd/Prompt de Comando): venv\Scripts\activate.bat
- Instalação do Django: pip install django
- Instalação da lib do postgreSQL: pip install psycopg2-binary
- Instalação do DRF: pip install djangorestframework
- Instalação da lib requests: pip install requests
## 3. Instalar o PostGRES
- Link do PostGRES: https://www.postgresql.org/download/

## 4. Instalar o Postman
- [Link para o Postman](https://www.postman.com/downloads/)

## 5. Rodar o Projeto
- Para rodar o servidor e testar os endpoints: python manage.py runserver

## 6. Para rodar os testes, use:
- python manage.py test

# Exemplos de Requests e Responses
## Treinadores
- [Collection Postman endpoints treinador](collectionEndpoints%20Treinador%20-%20postman_collection.json)
### Adicionar Treinador
#### Request
POST/http://127.0.0.1:8000/api/treinadores/
    ```
    

    {
    "nome": "Ash Ketchum",
    "idade": 10
    }
    ```
#### Response
    ```
    HTTP 201 Created
    Allow: GET, POST, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept

    {
        "id": 5,
        "nome": "Silvério",
        "idade": 30,
        "criado_em": "2025-11-15T18:39:59.600111Z",
        "atualizado_em": "2025-11-15T18:39:59.600133Z"
    }
    ```
## Pokémons
- TBD Collection Pokémon Postman
### Adicionar Pokémon
#### Request
POST http://127.0.0.1:8000/api/pokemons/
{"nome": "pikachu"}
#### Response
{
    "id": 4,
    "nome": "bulbasaur",
    "foto": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
    "altura": 7,
    "peso": 69,
    "criado_em": "2025-11-18T00:55:47.478232Z",
    "atualizado_em": "2025-11-18T00:55:47.478245Z"
}

# API
## Pokemon API
- https://pokeapi.co/
## Pokemon Picture
- https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/25.png

## Interface Django
- http://127.0.0.1:8000/api/treinadores/
