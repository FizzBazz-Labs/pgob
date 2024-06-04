from rest_framework.generics import ListAPIView

from rest_framework.permissions import IsAuthenticated

from helps.models import HelpSection
from helps.serializers import HelpSectionSerializer


class HelpSectionListView(ListAPIView):
    serializer_class = HelpSectionSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        user = self.request.user

        return HelpSection.objects \
            .prefetch_related('accreditation', 'items__group') \
            .filter(accreditation__in=user.accreditations.all(), items__group__in=user.groups.all()) \
            .distinct()
