from django.db.models import Q

from rest_framework import decorators, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from core.models import SiteConfiguration, Certification, AccreditationStatus
from core.views import ReviewAccreditationBase, AccreditationViewSet

from credentials.utils import certificate_accreditation

from national_accreditation.models import NationalAccreditation
from national_accreditation.serializers import NationalSerializer, NationalReadSerializer, NationalUpdateSerializer

from pgob_auth.permissions import IsReviewer, IsAccreditor, IsNewsletters

from .models import NationalAccreditation as National


class NationalViewSet(AccreditationViewSet):
    queryset = National.objects.all()
    serializer_class = NationalSerializer
    filterset_fields = ['status', 'country', 'certificated']

    def get_queryset(self):
        is_newsletters = IsNewsletters().has_permission(self.request, self)
        if not is_newsletters:
            return National.objects.all()

        choices = National.AccreditationType

        return National.objects.filter(
            Q(type=choices.NEWSLETTER_COMMITTEE) |
            Q(type=choices.COMMERCIAL_NEWSLETTER)
        )

    @decorators.action(detail=True, methods=['patch'])
    def certificate(self, request, pk=None, *args, **kwargs) -> Response:
        configuration = SiteConfiguration.objects.filter(available=True).first()
        if not configuration:
            return Response(
                {"error": "Site not available."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        try:
            item = National.objects.get(pk=pk)
            certificate_accreditation(configuration, 'nationals', item)
        except Certification.DoesNotExist:
            return Response(
                {"error": "Certification config not found."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except National.DoesNotExist:
            return Response(
                {"error": "National accreditation not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            {"message": "Accepted"},
            status=status.HTTP_202_ACCEPTED,
        )


class NationalListCreateApiView(ListCreateAPIView):
    queryset = NationalAccreditation.objects.all()
    serializer_class = NationalSerializer
    permission_classes = [IsAuthenticated]


class NationalRetrieveApiView(RetrieveUpdateAPIView):
    queryset = NationalAccreditation.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return NationalUpdateSerializer

        return NationalReadSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]

        return [IsAuthenticated()]


class ReviewAccreditation(ReviewAccreditationBase):
    model = NationalAccreditation
    serializer_class = NationalReadSerializer


class ApproveAccreditation(APIView):
    serializer_class = NationalReadSerializer
    permission_classes = [IsAuthenticated & IsAccreditor]

    def patch(self, request: Request, pk, *args, **kwargs):
        try:
            item = NationalAccreditation.objects.get(pk=pk)
            item.status = AccreditationStatus.APPROVED
            item.type = request.data.get('type')
            item.authorized_by = request.user
            item.authorized_comment = request.data.get('authorized_comment')
            item.save()

            serializer = self.serializer_class(item)
            return Response(serializer.data, status=HTTP_200_OK)

        except NationalAccreditation.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)


class RejectAccreditation(APIView):
    serializer_class = NationalReadSerializer
    permission_classes = [IsAuthenticated & (IsReviewer | IsAccreditor)]

    def patch(self, request: Request, pk, *args, **kwargs):
        try:
            item = NationalAccreditation.objects.get(pk=pk)
            item.status = AccreditationStatus.REJECTED
            item.rejected_by = request.user
            item.save()

            serializer = self.serializer_class(item)
            return Response(serializer.data, status=HTTP_200_OK)

        except NationalAccreditation.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
