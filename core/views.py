from django.db.models import Q, QuerySet

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from core.models import SiteConfiguration, AccreditationStatus
from core.serializers import SiteConfigurationSerializer
from core.mixins import (
    ApproveMixin,
    ReviewMixin,
    RejectMixin,
    CertificateMixin,
    ExportDataMixin,
    ImportDataMixin,
)

from pgob_auth.permissions import IsAdmin, IsReviewer, IsNewsletters, IsUser


class SiteConfigurationView(RetrieveUpdateAPIView):
    serializer_class = SiteConfigurationSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]

        return [IsAdmin()]

    def get_object(self):
        return SiteConfiguration.objects.first()


class ReviewAccreditationBase(APIView):
    model = None
    serializer_class = None
    permission_classes = [IsAuthenticated & IsReviewer]

    def patch(self, request: Request, pk, *args, **kwargs):
        try:
            item = self.model.objects.get(pk=pk)
            item.status = AccreditationStatus.REVIEWED
            item.reviewed_by = request.user
            item.reviewed_comment = request.data.get('reviewed_comment')
            item.save()

            serializer = self.serializer_class(item)
            return Response(serializer.data, status=HTTP_200_OK)

        except self.model.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)


class AccreditationViewSet(ApproveMixin, ReviewMixin, RejectMixin, ModelViewSet):
    permission_classes = [IsAuthenticated]

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


class ComplexAccreditationViewSet(CertificateMixin,
                                  ExportDataMixin,
                                  ImportDataMixin,
                                  AccreditationViewSet):
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
