import locale
from uuid import uuid4
from typing import Any
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

import qrcode

from django.conf import settings

from core.models import SiteConfiguration, Certification

from national_accreditation.models import NationalAccreditation as National
from international_accreditation.models import InternationalAccreditation as International

from overflight_non_commercial_aircraft.models import OverflightNonCommercialAircraft as Airfraft


def get_qr_code(data: str) -> Image:
    qr_code = qrcode.make(data)
    qr_buffer = BytesIO()
    qr_code.save(qr_buffer, format='PNG')
    qr_buffer.seek(0)

    return Image.open(qr_buffer).resize((175, 175))


def get_certification_data(
    configuration: SiteConfiguration,
    certification: Certification,
    accreditation: str,
    item: National | International,
) -> dict[str, Any]:
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

    accreditation_uuid = str(uuid4()).split('-')[0].upper()
    accreditation_type = str(Certification.AccreditationType(item.type).label)

    return {
        'president': configuration.president,
        'term_date': configuration.term_date.strftime('%d de %B de %Y'),
        'accreditation': accreditation,
        'type': accreditation_type,
        'color': certification.color,
        'text_color': certification.text_color,
        'fullname': f'{item.first_name} {item.last_name}',
        'profile': item.image,
        'pk': item.pk,
        'uuid': accreditation_uuid,
    }


def get_certification(data: dict[str, Any]) -> tuple[Image, Image]:
    template = settings.BASE_DIR / 'credentials' / \
        'static' / 'credentials' / 'base.png'

    image = Image.open(template)
    image_draw = ImageDraw.Draw(image)

    # Draw title
    title_font = ImageFont.load_default(30)
    title_position = (
        image.width - image_draw.textlength(data['president'], title_font))

    image_draw.text(
        (title_position / 2, 165),
        data['president'],
        fill='#002757',
        font=title_font,
        stroke_width=1,
        stroke_fill='#002757'
    )

    # Draw text
    term_date_font = ImageFont.load_default(20)
    term_date_position = (
        image.width - image_draw.textlength(data['term_date'], term_date_font))
    image_draw.text(
        (term_date_position / 2, 235),
        data['term_date'],
        fill='#002757',
        font=term_date_font,
        stroke_width=1,
        stroke_fill='#002757'
    )

    # Draw Profile
    profile = Image.open(data['profile']).resize((280, 280))

    image.paste(profile, (
        int((image.width - 280) / 2),
        280,
    ))

    fullname_font = ImageFont.load_default(45)
    fullname_position = image.width - \
        image_draw.textlength(data['fullname'], fullname_font)

    image_draw.text(
        (fullname_position / 2, 580),
        data['fullname'],
        fill='#002757',
        font=fullname_font,
        stroke_width=1,
        stroke_fill='#002757'
    )

    # Draw type box and title
    type_box = Image.new('RGBA', (image.width - 29, 100), data['color'])
    type_box_draw = ImageDraw.Draw(type_box)

    type_title_font = ImageFont.load_default(30)
    type_title_with = type_box.width - \
        type_box_draw.textlength(data['type'], type_title_font)

    type_box_draw.text(
        (type_title_with / 2, 30),
        data['type'],
        fill=data['text_color'],
        font=type_title_font,
    )

    image.paste(type_box, (19, image.height - 118))

    # Draw Temp Image QR code
    image_copy = image.copy()
    qr_found_data_image = get_qr_code(f'{settings.FRONTEND_DETAIL_URL}/404')
    image_copy.paste(qr_found_data_image, (
        int((image.width - 175) / 2),
        780,
    ))

    # Draw QR Code
    qr_image = get_qr_code(
        f'{settings.FRONTEND_DETAIL_URL}/{data['accreditation']}/{data['pk']}/?uuid={data['uuid']}')
    image.paste(qr_image, (
        int((image.width - 175) / 2),
        780,
    ))

    return image, image_copy


def certificate_accreditation(
    configuration: SiteConfiguration,
    accreditation: str,
    item: National | International,
):
    certification = Certification.objects.get(accreditation_type=item.type)

    data = get_certification_data(
        configuration, certification, accreditation, item)
    image, image_copy = get_certification(data)

    country = ''
    if accreditation == 'internationals':
        country = item.country.name.lower().replace(' ', '_')

    save_path = (
        settings.BASE_DIR /
        'certifications' /
        accreditation /
        country /
        str(data['type']).replace(' ', '_').lower()
    )

    if not save_path.exists():
        save_path.mkdir(parents=True)

    filename = f'{data['type']} {data['fullname']}'.replace(' ', '_').lower()
    image.save(save_path / f'{filename}.pdf')

    item.uuid = data['uuid']
    item.certificated = True

    image_bytes = BytesIO()
    image_copy.save(image_bytes, format='PNG')
    image_bytes.seek(0)

    item.certification.save(f'{filename}.png', image_bytes, save=False)

    item.save()


def draw_overflight_permission(pk: int):

    def draw_flight_type(flightType: str):
        if flightType == Airfraft.FlightType.FLIGHT:
            return (605, 390)
        else:
            return (605, 425)

    def draw_aircraft_type(aircraftType: str):
        if aircraftType == Airfraft.AircraftType.EMERGENCY:
            return (225, 510)
        elif aircraftType == Airfraft.AircraftType.AMBULANCE:
            return (418, 510)
        elif aircraftType == Airfraft.AircraftType.CHARTER:
            return (564, 510)
        elif aircraftType == Airfraft.AircraftType.MILITARY:
            return (700, 510)
        elif aircraftType == Airfraft.AircraftType.TECHNICAL_SCALE:
            return (1162, 510)
        else:
            return (0, 0)

    def draw_category(category: str):
        if category == Airfraft.Category.TECHNICIANS:
            return (190, 1005)
        elif category == Airfraft.Category.DIPLOMATS:
            return (400, 1005)
        elif category == Airfraft.Category.MILITARIES:
            return (585, 1005)
        elif category == Airfraft.Category.RESCUERS:
            return (977, 1005)
        elif category == Airfraft.Category.VOLUNTEERS:
            return (790, 1005)
        else:
            return (0, 0)

    data: Airfraft = Airfraft.objects.get(pk=pk)

    template = (settings.BASE_DIR / 'credentials' /
                'static' / 'credentials' / 'overflight_permission.jpg')

    image = Image.open(template)
    image_draw = ImageDraw.Draw(image)

    image_draw.text((160, 298), data.created_at.date().strftime('%Y-%m-%d'), fill='black',
                    font=ImageFont.load_default(20))

    image_draw.text((220, 357), data.created_by.get_full_name(), fill='black',
                    font=ImageFont.load_default(20))

    image_draw.text((920, 357), data.country.name, fill='black',
                    font=ImageFont.load_default(20))

    image_draw.text(draw_flight_type(data.flight_type), 'X', fill='black',
                    font=ImageFont.load_default(20))

    image_draw.text(draw_aircraft_type(data.aircraft_type), 'X',
                    fill='black', font=ImageFont.load_default(20))

    image_draw.text((278, 680), data.arrival_date.strftime(
        '%Y-%m-%d'), fill='black', font=ImageFont.load_default(19))

    image_draw.text((470, 680), data.arrival_date.time().strftime(
        '%H:%M'), fill='black', font=ImageFont.load_default(19))

    image_draw.text((860, 680), data.origin, fill='black',
                    font=ImageFont.load_default(20))

    image_draw.text((320, 740), data.model, fill='black',
                    font=ImageFont.load_default(20))

    image_draw.text((687, 740), data.registration, fill='black',
                    font=ImageFont.load_default(20))

    image_draw.text((1027, 740), data.get_aircraft_type_display(), fill='black',
                    font=ImageFont.load_default(20))

    image_draw.text((300, 795), data.call_sign, fill='black',
                    font=ImageFont.load_default(20))

    image_draw.text((280, 852), data.ground_facilities,
                    fill='black', font=ImageFont.load_default(20))

    image_draw.text((340, 913), str(data.passengers_count), fill='black',
                    font=ImageFont.load_default(20))

    image_draw.text((990, 913), data.destination, fill='black',
                    font=ImageFont.load_default(20))

    image_draw.text(draw_category(data.category), 'X',
                    fill='black', font=ImageFont.load_default(20))

    image.save('aircraft.pdf')
