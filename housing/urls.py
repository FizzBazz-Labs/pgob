from rest_framework.routers import DefaultRouter

from housing.views import HousingViewSet

router = DefaultRouter()

router.register(r'', HousingViewSet)

urlpatterns = router.urls
