import pypandoc
import jinja2

from django.http import HttpResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from docxtpl import DocxTemplate

from docx import Document

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

from core.models import SiteConfiguration, Certification, AccreditationStatus

from national_accreditation.models import NationalAccreditation as National
from international_accreditation.models import InternationalAccreditation as International
from general_vehicle_accreditation.models import GeneralVehicleAccreditation as GeneralVehicle

from .utils import certificate_accreditation, certificate_vehicle_accreditation

from vehicle_access_airport_accreditations.models import VehicleAccessAirportAccreditations

from intercom_equipment_declaration.models import IntercomEquipmentDeclaration

from security_accreditations.models import SecurityWeaponAccreditation


class CertificateView(APIView):
    def get(self, request: Request, accreditation: str, *args, **kwargs) -> Response:
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
                        certificate_accreditation(
                            configuration, accreditation, item)
            except Certification.DoesNotExist:
                return Response(
                    {"error": "Certification config not found."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return Response(
            {"message": "Accepted"},
            status=status.HTTP_202_ACCEPTED,
        )


def generate_pdf(request):
    doc = DocxTemplate('aeropuerto.docx')
    jinja_env = jinja2.Environment()

    context = VehicleAccessAirportAccreditations.objects.all().last()

    context = {
        'data': context,
    }

    doc.render(context, jinja_env)

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    attachment = f'attachment; filename=PdfAeropuerto.docx'
    response['Content-Disposition'] = attachment
    doc.save(response)
    return response


def generate_communication_equipment_pdf(request):
    doc = DocxTemplate('comunicacion.docx')
    jinja_env = jinja2.Environment()

    context = IntercomEquipmentDeclaration.objects.all().last()

    context = {
        'data': context,
    }

    doc.render(context, jinja_env)

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    attachment = f'attachment; filename=armas.docx'
    response['Content-Disposition'] = attachment
    doc.save(response)
    return response


def generate_weapons_pdf(request):
    doc = DocxTemplate('armas.docx')
    jinja_env = jinja2.Environment()

    context = SecurityWeaponAccreditation.objects.all().last()

    context = {
        'data': context,
    }

    doc.render(context, jinja_env)

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    attachment = f'attachment; filename=comunicacion.docx'
    response['Content-Disposition'] = attachment
    doc.save(response)
    return response
