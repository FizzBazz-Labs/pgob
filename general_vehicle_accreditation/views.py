from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK

from general_vehicle_accreditation.models import GeneralVehicleAccreditation
from general_vehicle_accreditation.serializers import GeneralVehicleAccreditationSerializer, \
    GeneralVehicleAccreditationReadSerializer

from core.models import AccreditationStatus
from core.views import ReviewAccreditationBase

from pgob_auth.permissions import IsReviewer, IsAccreditor


class GeneralVehicleAccreditationListApiView(ListCreateAPIView):
    queryset = GeneralVehicleAccreditation.objects.all()
    serializer_class = GeneralVehicleAccreditationSerializer
    permission_classes = [IsAuthenticated]


class GeneralVehicleAccreditationRetrieveApiView(RetrieveUpdateAPIView):
    queryset = GeneralVehicleAccreditation.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GeneralVehicleAccreditationReadSerializer

        return GeneralVehicleAccreditationSerializer


class ReviewAccreditation(ReviewAccreditationBase):
    model = GeneralVehicleAccreditation
    serializer_class = GeneralVehicleAccreditationSerializer


class ApproveAccreditation(APIView):
    serializer_class = GeneralVehicleAccreditationSerializer
    permission_classes = [IsAuthenticated & IsAccreditor]

    def patch(self, request: Request, pk, *args, **kwargs):
        try:
            item = GeneralVehicleAccreditation.objects.get(pk=pk)
            item.status = AccreditationStatus.APPROVED
            item.authorized_by = request.user
            item.save()

            serializer = self.serializer_class(item)
            return Response(serializer.data, status=HTTP_200_OK)

        except GeneralVehicleAccreditation.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)


class RejectAccreditation(APIView):
    serializer_class = GeneralVehicleAccreditationSerializer
    permission_classes = [IsAuthenticated & (IsReviewer | IsAccreditor)]

    def patch(self, request: Request, pk, *args, **kwargs):
        try:
            item = GeneralVehicleAccreditation.objects.get(pk=pk)
            item.status = AccreditationStatus.REJECTED
            item.rejected_by = request.user
            item.save()

            serializer = self.serializer_class(item)
            return Response(serializer.data, status=HTTP_200_OK)

        except GeneralVehicleAccreditation.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
