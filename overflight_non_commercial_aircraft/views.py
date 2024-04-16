from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK

from overflight_non_commercial_aircraft.models import OverflightNonCommercialAircraft
from overflight_non_commercial_aircraft.serializers import OverflightNonCommercialAircraftSerializer, \
    OverflightNonCommercialAircraftReadSerializer

from core.models import AccreditationStatus

from pgob_auth.permissions import IsReviewer, IsAccreditor


class OverflightNonCommercialAircraftCreateApiView(ListCreateAPIView):
    queryset = OverflightNonCommercialAircraft.objects.all()
    serializer_class = OverflightNonCommercialAircraftSerializer
    permission_classes = [IsAuthenticated]


class OverflightNonCommercialAircraftRetrieveApiView(RetrieveUpdateAPIView):
    queryset = OverflightNonCommercialAircraft.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return OverflightNonCommercialAircraftSerializer
        return OverflightNonCommercialAircraftReadSerializer

    permission_classes = [IsAuthenticated]


class ReviewAccreditation(APIView):
    serializer_class = OverflightNonCommercialAircraftReadSerializer
    permission_classes = [IsAuthenticated & IsReviewer]

    def patch(self, request: Request, pk, *args, **kwargs):
        try:
            item = OverflightNonCommercialAircraft.objects.get(pk=pk)
            item.status = AccreditationStatus.REVIEWED
            item.reviewed_by = request.user
            item.reviewed_comment = request.data.get('reviewed_comment')
            item.save()

            serializer = self.serializer_class(item)
            return Response(serializer.data, status=HTTP_200_OK)

        except OverflightNonCommercialAircraft.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)


class ApproveAccreditation(APIView):
    serializer_class = OverflightNonCommercialAircraftReadSerializer
    permission_classes = [IsAuthenticated & IsAccreditor]

    def patch(self, request: Request, pk, *args, **kwargs):
        try:
            item = OverflightNonCommercialAircraft.objects.get(pk=pk)
            item.status = AccreditationStatus.APPROVED
            item.authorized_by = request.user
            item.save()

            serializer = self.serializer_class(item)
            return Response(serializer.data, status=HTTP_200_OK)

        except OverflightNonCommercialAircraft.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)


class RejectAccreditation(APIView):
    serializer_class = OverflightNonCommercialAircraftReadSerializer
    permission_classes = [IsAuthenticated & (IsReviewer | IsAccreditor)]

    def patch(self, request: Request, pk, *args, **kwargs):
        try:
            item = OverflightNonCommercialAircraft.objects.get(pk=pk)
            item.status = AccreditationStatus.REJECTED
            item.rejected_by = request.user
            item.save()

            serializer = self.serializer_class(item)
            return Response(serializer.data, status=HTTP_200_OK)

        except OverflightNonCommercialAircraft.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
