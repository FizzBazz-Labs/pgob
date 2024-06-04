from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from core.models import SiteConfiguration, Certification, AccreditationStatus

from national_accreditation.models import NationalAccreditation as National
from international_accreditation.models import InternationalAccreditation as International
from general_vehicle_accreditation.models import GeneralVehicleAccreditation as GeneralVehicle

from .utils import certificate_accreditation, certificate_vehicle_accreditation


class CertificateView(APIView):
    def get(self, request: Request, accreditation: str, *args, **kwargs) -> Response:
        configuration = SiteConfiguration.objects.filter(available=True).first()
        if not configuration:
            return Response(
                {"error": "Site not available."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        match accreditation:
            case 'nationals':
                model = National
            case 'internationals':
                model = International
            case 'general-vehicles':
                model = GeneralVehicle

            case _:
                return Response(
                    {"error": "Invalid accreditation type."},
                    status=status.HTTP_400_BAD_REQUEST)

        items = model.objects.filter(
            status=AccreditationStatus.APPROVED,
            certificated=False)

        country = request.query_params.get('country')
        if country is not None:
            items = items.filter(country=country)

        if not items.exists():
            return Response(status=status.HTTP_204_NO_CONTENT)

        for item in items:
            try:
                match accreditation:
                    case 'general-vehicles':
                        certificate_vehicle_accreditation(item)
                    case _:
                        certificate_accreditation(configuration, accreditation, item)
            except Certification.DoesNotExist:
                return Response(
                    {"error": "Certification config not found."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return Response(
            {"message": "Accepted"},
            status=status.HTTP_202_ACCEPTED,
        )
