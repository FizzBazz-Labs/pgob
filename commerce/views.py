from core.views import AccreditationViewSet

from commerce.models import Commerce
from commerce.serializers import CommerceSerializer


class CommerceViewSet(AccreditationViewSet):
    queryset = Commerce.objects.all()
    serializer_class = CommerceSerializer
