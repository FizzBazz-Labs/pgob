from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK

from security_accreditations.models import SecurityWeaponAccreditation
from security_accreditations.serializers import SecurityWeaponAccreditationSerializer

from core.models import AccreditationStatus

from pgob_auth.permissions import IsReviewer, IsAccreditor


class SecurityWeaponAccreditationCreateApiView(ListCreateAPIView):
    queryset = SecurityWeaponAccreditation.objects.all()
    serializer_class = SecurityWeaponAccreditationSerializer
    permission_classes = [IsAuthenticated]


class SecurityWeaponAccreditationRetrieveApiView(RetrieveUpdateAPIView):
    queryset = SecurityWeaponAccreditation.objects.all()
    serializer_class = SecurityWeaponAccreditationSerializer
    permission_classes = [IsAuthenticated]


class ReviewAccreditation(APIView):
    serializer_class = SecurityWeaponAccreditationSerializer
    permission_classes = [IsAuthenticated & IsReviewer]

    def patch(self, request: Request, pk, *args, **kwargs):
        try:
            item = SecurityWeaponAccreditation.objects.get(pk=pk)
            item.status = AccreditationStatus.REVIEWED
            item.reviewed_by = request.user
            item.save()

            serializer = self.serializer_class(item)
            return Response(serializer.data, status=HTTP_200_OK)

        except SecurityWeaponAccreditation.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)


class ApproveAccreditation(APIView):
    serializer_class = SecurityWeaponAccreditationSerializer
    permission_classes = [IsAuthenticated & IsAccreditor]

    def patch(self, request: Request, pk, *args, **kwargs):
        try:
            item = SecurityWeaponAccreditation.objects.get(pk=pk)
            item.status = AccreditationStatus.APPROVED
            item.authorized_by = request.user
            item.save()

            serializer = self.serializer_class(item)
            return Response(serializer.data, status=HTTP_200_OK)

        except SecurityWeaponAccreditation.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)


class RejectAccreditation(APIView):
    serializer_class = SecurityWeaponAccreditationSerializer
    permission_classes = [IsAuthenticated & (IsReviewer | IsAccreditor)]

    def patch(self, request: Request, pk, *args, **kwargs):
        try:
            item = SecurityWeaponAccreditation.objects.get(pk=pk)
            item.status = AccreditationStatus.REJECTED
            item.rejected_by = request.user
            item.save()

            serializer = self.serializer_class(item)
            return Response(serializer.data, status=HTTP_200_OK)

        except SecurityWeaponAccreditation.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
