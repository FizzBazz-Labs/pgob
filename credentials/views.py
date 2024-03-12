import pdfkit
import environ
import os

from typing import Any

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from national_accreditation.models import NationalAccreditation

env = environ.Env(
    APP_HOST=(str, 'http://localhost:8000'),
)

env_file = os.path.join(settings.BASE_DIR, '.env')

if os.path.isfile(env_file):
    env.read_env(env_file)
else:
    raise Exception('No local .env detected.')


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
        'photo': f'{env('APP_HOST')}{image_url}',
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
