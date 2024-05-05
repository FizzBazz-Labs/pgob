import uuid
from typing import Any
from io import BytesIO
from PIL import Image

import pdfkit
import qrcode

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView

from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from national_accreditation.models import NationalAccreditation

from security_accreditations.models import SecurityWeaponAccreditation


def get_accreditation_color(accreditation_type: str) -> dict[str, Any]:
    accreditation_types = NationalAccreditation.AccreditationType

    if accreditation_type == accreditation_types.PROTOCOL:
        return {
            'footer_color': 'footer-grey',
            'arrow_color': 'arrow-grey',
        }
    elif accreditation_type == accreditation_types.SECURITY:
        return {
            'footer_color': 'footer-red',
            'arrow_color': 'arrow-red',
        }
    elif accreditation_type == accreditation_types.SUPPLIER:
        return {
            'footer_color': 'footer-green',
            'arrow_color': 'arrow-green',
        }
    else:
        return {
            'footer_color': 'footer-blue',
            'arrow_color': 'arrow-blue',
        }


def generate_pdf_response(image_url, color, type, qr_code, uuid) -> HttpResponse:
    context_data = {
        'type': _(type),
        'uuid': uuid,
        'qr_code': f'{settings.APP_HOST}{qr_code}',
        # TODO change hostname to production
        'photo': f'{settings.APP_HOST}{image_url}',
        'color': color,
    }

    html = render_to_string('credentials/credential.html', context_data)
    pdf = pdfkit.from_string(html, False)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="credential.pdf"'

    return response


class GenerateCredential(APIView):
    model = None

    def generate_qr_code(self, instance, pk) -> Image:

        if isinstance(instance, NationalAccreditation):
            qr_data = f'{settings.FRONTEND_DETAIL_URL}/nationals/{pk}'
        else:
            qr_data = f'{settings.FRONTEND_DETAIL_URL}/internationals/{pk}'
        qr_code = qrcode.make(qr_data)

        # Convert QR code to an image file suitable for an ImageField
        qr_buffer = BytesIO()
        qr_code.save(qr_buffer, format='PNG')
        qr_buffer.seek(0)

        return qr_buffer

    def set_uuid(self, instance, pk):
        new_uuid = str(uuid.uuid4())
        new_uuid = new_uuid.split('-')[0]

        instance.uuid = new_uuid
        instance.downloaded = True
        instance.save()

    def generate_weapon_pdf(self, pk) -> HttpResponse:
        weapon_accreditation = (
            SecurityWeaponAccreditation.objects
            .prefetch_related('weapons')
            .prefetch_related('communication_items')
            .get(pk=pk)
        )

        context = {
            'accreditation': weapon_accreditation,
        }

        html = render_to_string('credentials/weapon_credential.html', context)
        pdf = pdfkit.from_string(html, False)

        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="acreditacion_armas.pdf"'
        return response

    def get(self, request, pk, *args, **kwargs):
        try:
            accreditation = self.model.objects.get(pk=pk)

            if isinstance(accreditation, SecurityWeaponAccreditation):
                return self.generate_weapon_pdf(pk)

            self.set_uuid(accreditation, pk)

            # Generate QR code
            qr_buffer = self.generate_qr_code(accreditation, pk)
            filename = f'qr_code_{pk}.png'
            accreditation.qr_code.save(filename, qr_buffer, save=False)

            accreditation.save()
            accreditation_type = accreditation.type

            color = get_accreditation_color(accreditation.type)
            photo = accreditation.image.url

            return generate_pdf_response(photo, color, accreditation_type, accreditation.qr_code.url,
                                         accreditation.uuid)

        except self.model.DoesNotExist:
            return HttpResponse(status=HTTP_404_NOT_FOUND)


class TestTemplate(TemplateView):
    template_name = 'credentials/credential.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context_data = {
            'name': 'John Doe',
            'email': 'testing@gmail.com',
            'photo': 'https://www.w3schools.com/w3images/avatar2.png',
            'uuid': '12343-324324-234234-234234',
            'qr_code': 'https://www.w3schools.com/w3images/avatar2.png',
            'color': {
                'footer_color': 'footer-red',
                'arrow_color': 'arrow-red',
            },
            'type': 'PROTOCOL',
        }
        kwargs['photo'] = context_data['photo']
        kwargs['color'] = context_data['color']
        kwargs['type'] = context_data['type']
        kwargs['uuid'] = context_data['uuid']
        kwargs['qr_code'] = context_data['qr_code']
        return super().get_context_data(**kwargs)


class TestWeaponAccreditation(TemplateView):
    template_name = 'credentials/weapon_credential.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        pk = SecurityWeaponAccreditation.objects.last().pk

        weapon_accreditation = (
            SecurityWeaponAccreditation.objects
            .prefetch_related('weapons')
            .prefetch_related('communication_items')
            .get(pk=pk)
        )

        context['accreditation'] = weapon_accreditation

        return context


from PIL import Image, ImageDraw

from django.conf import settings

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response


class GenerateAccreditationView(APIView):
    def get(self, request: Request, *args, **kwargs) -> Response:
        path = settings.BASE_DIR / 'credentials' / 'static' / 'credentials' / 'images'

        image = Image.open(path / 'credentials.jpeg')

        draw = ImageDraw.Draw(image)
        draw.text((10, 10), 'Hello World', fill='black')

        image.save(path / 'credentials_edited.jpeg')

        return Response(status=status.HTTP_202_ACCEPTED)

# Save to mission folder

# Add menu action to generate accreditation
# Show modal and options
# Generate accreditation

# Add re-accreditate button only works with Accreditator, individual
