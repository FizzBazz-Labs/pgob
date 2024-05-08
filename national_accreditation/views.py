from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from core.models import AccreditationStatus
from core.views import ReviewAccreditationBase, ComplexAccreditationViewSet

from national_accreditation.models import NationalAccreditation
from national_accreditation.serializers import NationalSerializer, NationalReadSerializer, NationalUpdateSerializer

from pgob_auth.permissions import IsReviewer, IsAccreditor

from .models import NationalAccreditation as National


class NationalViewSet(ComplexAccreditationViewSet):
    queryset = National.objects.all()
    serializer_class = NationalSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['status', 'country', 'certificated']
    search_fields = ['first_name', 'last_name', 'created_at__date']


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
