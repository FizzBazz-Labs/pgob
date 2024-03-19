from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from core.models import AccreditationStatus
from national_accreditation.models import NationalAccreditation
from national_accreditation.serializers import NationalSerializer, NationalReadSerializer, NationalUpdateSerializer
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
            item = NationalAccreditation.objects.get(pk=pk)
            item.status = AccreditationStatus.REVIEWED
            item.reviewed_by = request.user
            item.save()

            serializer = self.serializer_class(item)
            return Response(serializer.data, status=HTTP_200_OK)

        except NationalAccreditation.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)


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
