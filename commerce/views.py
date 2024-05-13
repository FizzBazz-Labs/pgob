from rest_framework.viewsets import ModelViewSet

from core.views import AccreditationViewSet

from commerce.models import Commerce, CommerceEmployee
from commerce.serializers import CommerceSerializer, CommerceEmployeeSerializer


class CommerceViewSet(AccreditationViewSet):
    queryset = Commerce.objects.all()
    serializer_class = CommerceSerializer
    filterset_fields = ['status']
    search_fields = ['created_at__date']


class CommerceEmployeeViewSet(ModelViewSet):
    queryset = CommerceEmployee.objects.all()
    serializer_class = CommerceEmployeeSerializer
    filterset_fields = ['commerce']
    pagination_class = None
