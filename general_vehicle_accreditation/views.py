from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from core.models import Certification
from general_vehicle_accreditation.models import GeneralVehicleAccreditation as GeneralVehicle
from general_vehicle_accreditation.serializers import GeneralVehicleSerializer

from accreditations.views import AccreditationViewSet

from credentials.utils import certificate_vehicle_accreditation


class GeneralVehicleViewSet(AccreditationViewSet):
    queryset = GeneralVehicle.objects.all()
    serializer_class = GeneralVehicleSerializer
    filterset_fields = ['status', 'country']
    search_fields = ['created_at__date']

    @action(detail=True, methods=['patch'])
    def certificate(self, request: Request, pk=None, *args, **kwargs) -> Response:
        try:
            item = GeneralVehicle.objects.get(pk=pk)
            certificate_vehicle_accreditation(item)

            return Response(
                {"message": "Accepted"},
                status=status.HTTP_202_ACCEPTED,
            )

        except GeneralVehicle.DoesNotExist:
            return Response(
                {"error": "Certification config not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        except Certification.DoesNotExist:
            return Response(
                {"error": "Certification config not found."},
                status=status.HTTP_400_BAD_REQUEST,
            )
