from django.db.models import Prefetch, Q
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from helps.models import HelpSection, HelpSectionItem
from helps.serializers import HelpSectionSerializer


class HelpSectionListView(ListAPIView):
    serializer_class = HelpSectionSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        user = self.request.user

        accreditations = user.profile.accreditations.all()
        groups = user.groups.all()

        section_items_qs = HelpSectionItem.objects \
            .filter(groups__in=groups) \
            .distinct()

        return HelpSection.objects \
            .filter(accreditations__in=accreditations) \
            .distinct() \
            .prefetch_related(Prefetch('items', queryset=section_items_qs))
