from core.views import AccreditationViewSet

from housing.models import Housing
from housing.serializers import HousingSerializer


class HousingViewSet(AccreditationViewSet):
    queryset = Housing.objects.all()
    serializer_class = HousingSerializer
