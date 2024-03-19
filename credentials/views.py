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
        return 'black'


def generate_pdf_response(image_url, color, type) -> HttpResponse:
    context_data = {
        'type': _(type),
        # TODO change hostname to production
        'photo':f'{settings.APP_HOST}{image_url}',
        'color': color,
    }

    html = render_to_string('credentials/credential.html', context_data)
    pdf = pdfkit.from_string(html, False)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="credential.pdf"'

    return response


class GenerateCredential(APIView):
    model = None

    def get(self, request, pk, *args, **kwargs):
        try:
            accreditation = self.model.objects.get(pk=pk)

            accreditation.uuid = uuid.uuid4()
            accreditation.downloaded = True

            # Generate QR code
            if isinstance(accreditation, NationalAccreditation):
                qr_data = f'{settings.FRONTEND_DETAIL_URL}/nationals/{pk}'
            else:
                qr_data = f'{settings.FRONTEND_DETAIL_URL}/internationals/{pk}'
            qr_code = qrcode.make(qr_data)

            # Convert QR code to an image file suitable for an ImageField
            qr_buffer = BytesIO()
            qr_code.save(qr_buffer, format='PNG')
            qr_buffer.seek(0)

            # The name of the image file (e.g., 'qr_code.png')
            filename = f'qr_code_{pk}.png'
            accreditation.qr_code.save(filename, qr_buffer, save=False)

            accreditation.save()
            accreditation_type = accreditation.type

            color = get_accreditation_color(accreditation.type)
            photo = accreditation.image.url

            return generate_pdf_response(photo, color, accreditation_type)

        except self.model.DoesNotExist:
            return HttpResponse(status=HTTP_404_NOT_FOUND)


class TestTemplate(TemplateView):
    template_name = 'credentials/test.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context_data = {
            'name': 'John Doe',
            'email': 'testing@gmail.com',
            'photo': 'https://www.w3schools.com/w3images/avatar2.png',
            'color': {
                'footer_color': 'footer-red',
                'arrow_color': 'arrow-red',
            },
            'type': 'PROTOCOL',
        }
        kwargs['photo'] = context_data['photo']
        kwargs['color'] = context_data['color']
        kwargs['type'] = context_data['type']
        return super().get_context_data(**kwargs)
