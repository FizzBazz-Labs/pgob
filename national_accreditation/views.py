from django.db.models import Q

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from core.models import AccreditationStatus
from core.views import ReviewAccreditationBase, ComplexAccreditationViewSet

from national_accreditation.models import NationalAccreditation
from national_accreditation.serializers import NationalSerializer, NationalReadSerializer, NationalUpdateSerializer

from pgob_auth.permissions import IsReviewer, IsAccreditor, IsNewsletters

from .models import NationalAccreditation as National


class NationalViewSet(ComplexAccreditationViewSet):
    queryset = National.objects.all()
    serializer_class = NationalSerializer
    filterset_fields = ['status', 'country', 'certificated']
    search_fields = ['first_name', 'last_name', 'created_at__date']

    def get_queryset(self):
        queryset = super().get_queryset()

        is_newsletters = IsNewsletters().has_permission(self.request, self)
        if not is_newsletters:
            return queryset

        choices = National.AccreditationType

        return queryset.filter(
            Q(type=choices.COMMERCIAL_NEWSLETTER) |
            Q(type=choices.NEWSLETTER_COMMITTEE)
        )

    def update(self, request, *args, **kwargs):
        if self.get_object().times_edited > 0:

            return Response({'error': 'You can not update this accreditation.'}, status=HTTP_400_BAD_REQUEST)

        instance = self.get_object()
        if instance.times_edited == 0:
            instance.times_edited += 1
            instance.save()

        return super().update(request, *args, **kwargs)


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
