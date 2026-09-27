from rest_framework.routers import DefaultRouter
from .views import DishViewSet

router = DefaultRouter()
router.register("dishes", DishViewSet)

urlpatterns = router.urls