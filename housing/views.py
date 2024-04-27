from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from housing.models import Housing
from housing.serializers import HousingSerializer


class HousingViewSet(ModelViewSet):
    queryset = Housing.objects.all()
    serializer_class = HousingSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            return [AllowAny()]

        return [IsAuthenticated()]
