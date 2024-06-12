import pandas as pd
from django.db.models import QuerySet
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

from core import utils

from pgob_auth.permissions import IsUser


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

    def filter_queryset(self, queryset):
        date_filter = self.request.query_params.get('date')
        get_queryset = super().filter_queryset(queryset)

        if date_filter:
            get_queryset = get_queryset.filter(created_at__date=date_filter)

        return get_queryset


class ComplexAccreditationViewSet(CertificateMixin, ExportDataMixin, ImportDataMixin, AccreditationViewSet):
    pass
