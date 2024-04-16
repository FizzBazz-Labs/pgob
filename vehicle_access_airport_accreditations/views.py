from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.permissions import IsAuthenticated

from core.models import AccreditationStatus
from core.views import ReviewAccreditationBase

from pgob_auth.permissions import IsAccreditor, IsReviewer

from vehicle_access_airport_accreditations.models import VehicleAccessAirportAccreditations
from vehicle_access_airport_accreditations.serializers import (
    VehicleAccessAirportAccreditationsSerializer,
    VehicleAccessAirportAccreditationsReadSerializer)


class VehicleAccessAirportAccreditationsListCreateApiView(ListCreateAPIView):
    queryset = VehicleAccessAirportAccreditations.objects.all()
    serializer_class = VehicleAccessAirportAccreditationsSerializer
    permission_classes = [IsAuthenticated]


class VehicleAccessAirportAccreditationsRetrieveApiView(RetrieveUpdateAPIView):
    queryset = VehicleAccessAirportAccreditations.objects.all()
    serializer_class = VehicleAccessAirportAccreditationsSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return VehicleAccessAirportAccreditationsReadSerializer
        return VehicleAccessAirportAccreditationsSerializer


class ReviewAccreditation(ReviewAccreditationBase):
    model = VehicleAccessAirportAccreditations
    serializer_class = VehicleAccessAirportAccreditationsReadSerializer


class ApproveAccreditation(APIView):
    serializer_class = VehicleAccessAirportAccreditationsReadSerializer
    permission_classes = [IsAuthenticated & IsAccreditor]

    def patch(self, request: Request, pk, *args, **kwargs):
        try:
            item = VehicleAccessAirportAccreditations.objects.get(pk=pk)
            item.status = AccreditationStatus.APPROVED
            item.authorized_by = request.user
            item.save()

            serializer = self.serializer_class(item)
            return Response(serializer.data, status=HTTP_200_OK)

        except VehicleAccessAirportAccreditations.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)


class RejectAccreditation(APIView):
    serializer_class = VehicleAccessAirportAccreditationsReadSerializer
    permission_classes = [IsAuthenticated & (IsReviewer | IsAccreditor)]

    def patch(self, request: Request, pk, *args, **kwargs):
        try:
            item = VehicleAccessAirportAccreditations.objects.get(pk=pk)
            item.status = AccreditationStatus.REJECTED
            item.rejected_by = request.user
            item.save()

            serializer = self.serializer_class(item)
            return Response(serializer.data, status=HTTP_200_OK)

        except VehicleAccessAirportAccreditations.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
