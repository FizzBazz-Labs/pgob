from django.db.models import Q

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from core.models import AccreditationStatus
from core.views import ReviewAccreditationBase, ComplexAccreditationViewSet

from international_accreditation.models import InternationalAccreditation
from international_accreditation.serializers import (
    InternationalAccreditationSerializer,
    InternationalAccreditationReadSerializer,
    InternationalAccreditationUpdateSerializer)

from pgob_auth.permissions import IsReviewer, IsAccreditor, IsNewsletters

from .models import InternationalAccreditation as International


class InternationalViewSet(ComplexAccreditationViewSet):
    queryset = International.objects.all()
    serializer_class = InternationalAccreditationSerializer
    filterset_fields = ['status', 'country', 'certificated']
    search_fields = ['first_name', 'last_name']

    def get_queryset(self):
        queryset = super().get_queryset()

        is_newsletters = IsNewsletters().has_permission(self.request, self)
        if not is_newsletters:
            return queryset

        choices = International.AccreditationType

        return queryset.filter(
            Q(type=choices.OFFICIAL_NEWSLETTER) |
            Q(type=choices.COMMERCIAL_NEWSLETTER)
        )


class InternationalListCreateApiView(ListCreateAPIView):
    queryset = InternationalAccreditation.objects.all()
    serializer_class = InternationalAccreditationSerializer
    permission_classes = [IsAuthenticated]


class InternationalRetrieveApiView(RetrieveUpdateAPIView):
    queryset = InternationalAccreditation.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return InternationalAccreditationUpdateSerializer

        return InternationalAccreditationReadSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]

        return [IsAuthenticated()]


class ReviewAccreditation(ReviewAccreditationBase):
    model = InternationalAccreditation
    serializer_class = InternationalAccreditationReadSerializer


class ApproveAccreditation(APIView):
    serializer_class = InternationalAccreditationReadSerializer
    permission_classes = [IsAuthenticated & IsAccreditor]

    def patch(self, request: Request, pk, *args, **kwargs):
        try:
            item = InternationalAccreditation.objects.get(pk=pk)
            item.status = AccreditationStatus.APPROVED
            item.type = request.data.get('type')
            item.authorized_by = request.user
            item.authorized_comment = request.data.get('authorized_comment')
            item.save()

            serializer = self.serializer_class(item)
            return Response(serializer.data, status=HTTP_200_OK)

        except InternationalAccreditation.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)


class RejectAccreditation(APIView):
    serializer_class = InternationalAccreditationReadSerializer
    permission_classes = [IsAuthenticated & (IsReviewer | IsAccreditor)]

    def patch(self, request: Request, pk, *args, **kwargs):
        try:
            item = InternationalAccreditation.objects.get(pk=pk)
            item.status = AccreditationStatus.REJECTED
            item.rejected_by = request.user
            item.save()

            serializer = self.serializer_class(item)
            return Response(serializer.data, status=HTTP_200_OK)

        except InternationalAccreditation.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
