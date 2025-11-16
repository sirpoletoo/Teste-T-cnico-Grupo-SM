from django.db import models

class Treinador(models.Model):
    """
    Modelo para representar um Treinador de Pokémon.
    """
    nome = models.CharField(
        max_length=100,
        help_text="Nome completo do treinador."
    )
    idade = models.IntegerField(
        help_text="Idade do treinador."
    )
    criado_em = models.DateTimeField(
        auto_now_add=True,
        help_text="Data de criação do registro."
    )
    atualizado_em = models.DateTimeField(
        auto_now=True,
        help_text="Data da última atualização do registro."
    )

    class Meta:
        verbose_name = "Treinador"
        verbose_name_plural = "Treinadores"
        ordering = ['nome']

    def __str__(self):
        return f"Treinador: {self.nome} ({self.id})"

class Pokemon(models.Model):
    """
    Modelo para representar um Pokémon, a foto, altura e peso serão preenchidos pela PokeAPI.
    """
    nome = models.CharField(
        max_length=100,
        unique=True, # evitar duplicidade pelo nome
        help_text="Nome do Pokémon, usado para buscar na PokeAPI"
    )
    foto = models.URLField(
        blank=True,
        null=True,
        help_text="URL da imagem do Pokémon (decímetros)"
    )
    altura = models.IntegerField(
        default=0,
        help_text="Peso do Pokémon (hectogramas)"
    )
    peso = models.IntegerField(
        default=0,
        help_text="Peso do Pokémon(hectogramas)"
    )
    criado_em = models.DateTimeField(
        auto_now_add=True
    )
    atualizado_em = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Pokémon"
        verbose_name_plural = "Pokémons"
        ordering = ['nome']

    def __str__(self):
        return f"Pokémon: {self.nome}"