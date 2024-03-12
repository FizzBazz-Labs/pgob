from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.request import Request
from rest_framework.response import Response

from national_accreditation.models import NationalAccreditation
from national_accreditation.serializers import NationalSerializer, NationalReadSerializer, NationalUpdateSerializer

from core.models import AccreditationStatus
from pgob_auth.permissions import IsReviewer, IsAccreditor


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

    permission_classes = [IsAuthenticated]


class ReviewAccreditation(APIView):
    serializer_class = NationalReadSerializer
    permission_classes = [IsAuthenticated & IsReviewer]

    def patch(self, request: Request, pk, *args, **kwargs):
        try:
            national = NationalAccreditation.objects.get(pk=pk)
            national.status = AccreditationStatus.REVIEWED
            national.reviewed_by = request.user
            national.save()

            serializer = self.serializer_class(national)
            return Response(serializer.data, status=HTTP_200_OK)

        except NationalAccreditation.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)


class ApproveAccreditation(APIView):
    serializer_class = NationalReadSerializer
    permission_classes = [IsAuthenticated & IsAccreditor]

    def patch(self, request: Request, pk, *args, **kwargs):
        accreditation_type = request.data.get('type')

        try:
            national = NationalAccreditation.objects.get(pk=pk)
            national.status = AccreditationStatus.APPROVED
            national.type = request.data.get('type')
            national.authorized_by = request.user
            national.save()

            serializer = self.serializer_class(national)
            return Response(serializer.data, status=HTTP_200_OK)

        except NationalAccreditation.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)


class RejectAccreditation(APIView):
    serializer_class = NationalReadSerializer
    permission_classes = [IsAuthenticated & (IsReviewer | IsAccreditor)]

    def patch(self, request: Request, pk, *args, **kwargs):
        try:
            national = NationalAccreditation.objects.get(pk=pk)
            national.status = AccreditationStatus.REJECTED
            national.rejected_by = request.user
            national.save()

            serializer = self.serializer_class(national)
            return Response(serializer.data, status=HTTP_200_OK)

        except NationalAccreditation.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
