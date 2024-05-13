from django.db.models import Q, QuerySet
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from accreditations.mixins import (
    ApproveMixin,
    ReviewMixin,
    RejectMixin,
    CertificateMixin,
    ExportDataMixin,
    ImportDataMixin,
)

from pgob_auth.permissions import IsNewsletters, IsUser


class AccreditationViewSet(ApproveMixin, ReviewMixin, RejectMixin, ModelViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend]

    def get_queryset(self) -> QuerySet:
        is_user = IsUser().has_permission(self.request, self)
        if is_user:
            return self.queryset.filter(created_by=self.request.user)

        return super().get_queryset()

    def get_permissions(self):
        match self.action:
            case 'retrieve':
                permissions = [AllowAny]

            case _:
                permissions = self.permission_classes

        return [permission() for permission in permissions]


class ComplexAccreditationViewSet(CertificateMixin, ExportDataMixin, ImportDataMixin, AccreditationViewSet):
    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()

        is_newsletters = IsNewsletters().has_permission(self.request, self)
        if not is_newsletters:
            return queryset

        choices = queryset.model.AccreditationType

        return queryset.filter(
            Q(type=choices.NEWSLETTER_COMMITTEE) |
            Q(type=choices.COMMERCIAL_NEWSLETTER)
        )
