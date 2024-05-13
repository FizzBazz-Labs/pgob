from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from core.views import AccreditationViewSet

from housing.models import Housing, HousingPerson
from housing.serializers import HousingSerializer, HousingPersonSerializer


class HousingViewSet(AccreditationViewSet):
    queryset = Housing.objects.all()
    serializer_class = HousingSerializer
    filterset_fields = ['status']
    search_fields = ['created_at__date']


class HousingPersonViewSet(ModelViewSet):
    queryset = HousingPerson.objects.all()
    serializer_class = HousingPersonSerializer
    filterset_fields = ['housing']
    pagination_class = None
