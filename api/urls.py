from .views import PetViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', PetViewSet, base_name='pets')
urlpatterns = router.urls
