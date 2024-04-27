from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from commerce.models import Commerce
from commerce.serializers import CommerceSerializer


class CommerceViewSet(viewsets.ModelViewSet):
    queryset = Commerce.objects.all()
    serializer_class = CommerceSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            return [AllowAny()]

        return [IsAuthenticated()]
