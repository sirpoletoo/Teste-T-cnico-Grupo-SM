from rest_framework.routers import DefaultRouter
from .views import TreinadorViewSet

router = DefaultRouter()
router.register(r'treinadores', TreinadorViewSet)

urlpatterns = router.urls
