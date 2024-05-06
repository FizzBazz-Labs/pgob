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


import qrcode
from PIL import Image, ImageDraw, ImageFont

from django.conf import settings

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from national_accreditation.models import NationalAccreditation as National


class GenerateAccreditationView(APIView):
    def get(self, request: Request, *args, **kwargs) -> Response:
        item: National = National.objects.first()

        path = settings.BASE_DIR / 'credentials' / 'static' / 'credentials'

        image = Image.open(path / 'base.png')
        image_draw = ImageDraw.Draw(image)

        # Draw title
        title = u'Javier Ordoñez'
        title_font = ImageFont.load_default(30)
        image_draw.text(
            ((image.width - image_draw.textlength(title, title_font)) / 2, 165),
            title,
            fill='#002757',
            font=title_font,
            stroke_width=1,
            stroke_fill='#002757'
        )

        # Draw text
        date = u'1 de julio de 2024'
        date_font = ImageFont.load_default(20)
        image_draw.text(
            ((image.width - image_draw.textlength(date, date_font)) / 2, 235),
            date,
            fill='#002757',
            font=date_font,
            stroke_width=1,
            stroke_fill='#002757'
        )

        # Draw Profile
        profile_image = Image.open(item.image)
        profile_image = profile_image.resize((280, 280))
        image.paste(profile_image, (
            int((image.width - 280) / 2),
            280,
        ))

        profile_fullname = f'{item.first_name} {item.last_name}'
        profile_fullname_font = ImageFont.load_default(45)
        profile_fullname_position = image.width - image_draw.textlength(profile_fullname, profile_fullname_font)
        image_draw.text(
            (profile_fullname_position / 2, 580),
            profile_fullname,
            fill='#002757',
            font=profile_fullname_font,
            stroke_width=1,
            stroke_fill='#002757'
        )

        # Draw QR code
        qr_code = qrcode.make('Hello World!')
        qr_buffer = BytesIO()
        qr_code.save(qr_buffer, format='PNG')
        qr_buffer.seek(0)

        qr_code_image = Image.open(qr_buffer)
        qr_code_image = qr_code_image.resize((175, 175))

        image.paste(qr_code_image, (
            int((image.width - 175) / 2),
            780,
        ))

        # Draw type box and title
        type_box = Image.new('RGBA', (image.width - 29, 100), "black")
        type_box_draw = ImageDraw.Draw(type_box)
        type_title = u'ACREDITACIÓN DE SEGURIDAD'
        type_title_font = ImageFont.load_default(30)
        type_title_with = type_box.width - type_box_draw.textlength(type_title, type_title_font)

        type_box_draw.text(
            (type_title_with / 2, 30),
            type_title,
            fill='white',
            font=type_title_font,
        )

        image.paste(type_box, (19, image.height - 118))

        image.save(path / 'edited.png')
        return Response(status=status.HTTP_202_ACCEPTED)

# Save to mission folder

# Add menu action to generate accreditation
# Show modal and options
# Generate accreditation

# Add re-accreditate button only works with Accreditator, individual
