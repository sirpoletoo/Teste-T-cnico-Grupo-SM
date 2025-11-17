from rest_framework.routers import DefaultRouter
from .views import TreinadorViewSet

router = DefaultRouter()
router.register(r'treinadores', TreinadorViewSet, basename='treinador')

urlpatterns = router.urls