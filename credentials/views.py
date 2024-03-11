import pdfkit

from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views.generic import TemplateView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class GenerateCredential(APIView):

    def get(self, request):
        context_data = {
            'name': 'John Doe',
            'email': 'testing@gmail.com'
        }

        html = render_to_string('credentials/test.html', context_data)

        pdf = pdfkit.from_string(html, False)

        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="credential.pdf"'
        return response


class TestTemplate(TemplateView):
    template_name = 'credentials/test.html'
