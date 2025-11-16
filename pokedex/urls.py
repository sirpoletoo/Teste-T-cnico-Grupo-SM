from rest_framework.routers import DefaultRouter
from .views import TreinadorViewSet, PokemonViewSet

router = DefaultRouter()
router.register(r'treinadores', TreinadorViewSet)
router.register(r'pokemons', PokemonViewSet)

urlpatterns = router.urls
