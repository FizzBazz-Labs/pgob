from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from core.models import AccreditationStatus
from international_accreditation.models import InternationalAccreditation
from international_accreditation.serializers import InternationalAccreditationSerializer, \
    InternationalAccreditationReadSerializer, InternationalAccreditationUpdateSerializer
from pgob_auth.permissions import IsReviewer, IsAccreditor


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

    permission_classes = [IsAuthenticated]


class ReviewAccreditation(APIView):
    serializer_class = InternationalAccreditationReadSerializer
    permission_classes = [IsAuthenticated & IsReviewer]

    def patch(self, request: Request, pk, *args, **kwargs):
        try:
            item = InternationalAccreditation.objects.get(pk=pk)
            item.status = AccreditationStatus.REVIEWED
            item.reviewed_by = request.user
            item.save()

            serializer = self.serializer_class(item)
            return Response(serializer.data, status=HTTP_200_OK)

        except InternationalAccreditation.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)


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
