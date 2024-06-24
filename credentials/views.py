import jinja2

from docxtpl import DocxTemplate

from django.http import HttpResponse
from django.db import models

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response

from core.models import SiteConfiguration, Certification, AccreditationStatus
from national_accreditation.models import NationalAccreditation as National
from international_accreditation.models import InternationalAccreditation as International
from general_vehicle_accreditation.models import GeneralVehicleAccreditation as GeneralVehicle

from vehicle_access_airport_accreditations.models import VehicleAccessAirportAccreditations
from intercom_equipment_declaration.models import IntercomEquipmentDeclaration
from security_accreditations.models import SecurityWeaponAccreditation

from credentials.models import VehicleCertification
from credentials.utils import certificate_accreditation, certificate_vehicle_accreditation
from credentials.serializers import VehicleCertificationSerializer


class VehicleCertificationViewSet(ReadOnlyModelViewSet):
    queryset = VehicleCertification.objects.all()
    serializer_class = VehicleCertificationSerializer
    pagination_class = None


class CertificateView(APIView):
    @staticmethod
    def generate_pdf(request, model: models.Model, filename: str) -> HttpResponse:
        doc = DocxTemplate(filename)
        jinja_env = jinja2.Environment()

        context = model.objects.all().last()

        context = {'data': context}

        doc.render(context, jinja_env)

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        attachment = f'attachment; filename=PdfAeropuerto.docx'
        response['Content-Disposition'] = attachment
        doc.save(response)

        return response

    def get(self, request: Request, accreditation: str, *args, **kwargs) -> Response | HttpResponse:
        configuration = SiteConfiguration.objects.filter(
            available=True).first()
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
            case 'access-airport':
                model = VehicleAccessAirportAccreditations
            case 'communication-equipment':
                model = IntercomEquipmentDeclaration
            case 'securities':
                model = SecurityWeaponAccreditation

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
                    case 'nationals' | 'internationals':
                        certificate_accreditation(
                            configuration,
                            accreditation,
                            item,
                        )
                    case 'access-airport' | 'communication-equipment' | 'securities':
                        return self.generate_pdf(request, model, f'{accreditation}.docx')

            except Certification.DoesNotExist:
                return Response(
                    {"error": "Certification config not found."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return Response(
            {"message": "Accepted"},
            status=status.HTTP_202_ACCEPTED,
        )
