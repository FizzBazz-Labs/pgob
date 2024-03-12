from typing import Any

import pdfkit
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
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
        'photo': f'http://localhost:8000{image_url}',
        'color': color,
    }

    html = render_to_string('credentials/credential.html', context_data)
    pdf = pdfkit.from_string(html, False)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="credential.pdf"'
    return response


class GenerateNationalCredential(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        accreditation = NationalAccreditation.objects.get(pk=pk)
        accreditation_type = accreditation.type
        color = get_accreditation_color(accreditation_type)
        photo = accreditation.image.url
        return generate_pdf_response(photo, color, accreditation_type)


class GenerateCredential(APIView):
    model = None

    def get(self, request, pk, *args, **kwargs):
        accreditation = self.model.objects.get(pk=pk)
        accreditation_type = accreditation.type

        color = get_accreditation_color(accreditation.type)
        photo = accreditation.image.url

        return generate_pdf_response(photo, color, accreditation_type)


# class GenerateCredential(APIView):

#     def get_accreditation_color(self, accreditation_type: str) -> dict[str, Any]:
#         accreditation_types = NationalAccreditation.AccreditationType

#         if accreditation_type == accreditation_types.PROTOCOL:
#             return {
#                 'footer_color': 'footer-grey',
#                 'arrow_color': 'arrow-grey',
#             }
#         elif accreditation_type == accreditation_types.SECURITY:
#             return {
#                 'footer_color': 'footer-red',
#                 'arrow_color': 'arrow-red',
#             }
#         elif accreditation_type == accreditation_types.SUPPLIER:
#             return {
#                 'footer_color': 'footer-green',
#                 'arrow_color': 'arrow-green',
#             }
#         else:
#             return 'black'

#     def get(self, request, *args, **kwargs):
#         test = NationalAccreditation.objects.get(pk=kwargs['pk'])
#         accreditation_type = test.type

#         context_data = {
#             'name': 'John Doe',
#             'email': 'testing@gmail.com',
#             'type': accreditation_type.upper(),
#             'photo': f'http://localhost:8000{test.image.url}',
#             'color': self.get_accreditation_color(accreditation_type),
#         }

#         html = render_to_string('credentials/test.html', context_data)

#         pdf = pdfkit.from_string(html, False)

#         response = HttpResponse(pdf, content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="credential.pdf"'
#         return response


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
