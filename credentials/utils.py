import locale
import jinja2
import os
import qrcode

from uuid import uuid4
from typing import Any
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ExifTags
from docxtpl import DocxTemplate

from django.conf import settings
from django.core.files import File
from django.db import models

from core.models import SiteConfiguration, Certification
from core.utils import convert_docx_to_pdf

from national_accreditation.models import NationalAccreditation as National
from international_accreditation.models import InternationalAccreditation as International
from general_vehicle_accreditation.models import GeneralVehicleAccreditation as GeneralVehicle
from overflight_non_commercial_aircraft.models import OverflightNonCommercialAircraft as Aircfraft

from datetime import datetime
from pathlib import Path


def get_image_font(size: int) -> ImageFont:
    try:
        path = settings.BASE_DIR / 'credentials' / \
            'static' / 'credentials' / 'Avenir-Book.ttf'
        return ImageFont.truetype(path, size=size, encoding='utf-8')

    except OSError as e:
        return ImageFont.load_default(size)


def get_qr_code(data: str, size: tuple[int, int] = None) -> Image:
    if size is None:
        size = (275, 275)

    qr_code = qrcode.make(data)
    qr_buffer = BytesIO()
    qr_code.save(qr_buffer, format='PNG')
    qr_buffer.seek(0)

    return Image.open(qr_buffer).resize(size)


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
        'first_name': item.first_name,
        'last_name': item.last_name,
        'profile': item.image,
        'pk': item.pk,
        'uuid': accreditation_uuid,
    }


def adjust_image_orientation(image):
    """
    Adjusts the orientation of an image based on its EXIF data.
    """
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = image._getexif()
        if exif is not None:
            orientation = exif.get(orientation)
            if orientation == 3:
                image = image.rotate(180, expand=True)
            elif orientation == 6:
                image = image.rotate(270, expand=True)
            elif orientation == 8:
                image = image.rotate(90, expand=True)
    except Exception as e:
        # Log the exception if needed
        print(f"Error adjusting image orientation: {e}")
    return image


def get_certification(data: dict[str, Any]) -> tuple[Image, Image]:
    offset = 100
    template = settings.BASE_DIR / 'credentials' / \
        'static' / 'credentials' / 'base.jpg'

    image = Image.open(template)
    image_draw = ImageDraw.Draw(image)

    # Draw title
    title = data['president']
    title_font = get_image_font(60)
    title_position = (image.width - image_draw.textlength(title, title_font))

    image_draw.text(
        (title_position / 2, 375 - offset),
        title,
        fill='#808080',
        font=title_font,
        stroke_width=1,
        stroke_fill='#808080'
    )

    # Draw subtitle
    subtitle = 'Presidente de la República'
    subtitle_font = get_image_font(35)
    subtitle_position = (
        image.width - image_draw.textlength(subtitle, subtitle_font))

    image_draw.text(
        (subtitle_position / 2, 450 - offset),
        subtitle,
        fill='#808080',
        font=subtitle_font,
        stroke_width=1,
        stroke_fill='#808080'
    )

    # Draw text
    term_date = data['term_date']
    term_date_font = get_image_font(35)
    term_date_position = (
        image.width - image_draw.textlength(term_date, term_date_font))

    image_draw.text(
        (term_date_position / 2, 495 - offset),
        term_date,
        fill='#808080',
        font=term_date_font,
    )

    # Draw Profile
    # p_width, p_height = 400, 400
    #
    # profile = Image.open(data['profile']).resize((p_width, p_height))
    # mask = Image.new('L', (p_width, p_height), 0)
    # draw = ImageDraw.Draw(mask)
    # draw.ellipse((0, 0, p_width, p_height), fill=255)
    # profile_round = Image.new('RGBA', (p_width, p_height))
    # profile_round.paste(profile, (0, 0), mask=mask)
    #
    # image.paste(
    #     profile_round,
    #     (int((image.width - p_width) / 2), 600 - offset),
    #     mask=profile_round
    # )

    # Draw Profile
    p_width, p_height = 300, 400

    profile = Image.open(data['profile'])
    profile = adjust_image_orientation(profile)
    profile = profile.resize((p_width, p_height))
    mask = Image.new('L', (p_width, p_height), 0)
    draw = ImageDraw.Draw(mask)

    # Draw a rectangle with rounded corners on the mask
    round_rectangle = [(0, 0), (p_width, p_height)]
    corner_radius = 30  # adjust this value according to your needs
    draw.rounded_rectangle(round_rectangle, corner_radius, fill=255)

    profile_round = Image.new('RGBA', (p_width, p_height))
    profile_round.paste(profile, (0, 0), mask=mask)

    image.paste(
        profile_round,
        (int((image.width - p_width) / 2), 600 - offset),
        mask=profile_round
    )

    # Draw Fullname
    fullname = data['fullname']
    first_name = data['first_name']
    last_name = data['last_name']

    fullname_font = get_image_font(60)
    fullname_position = image.width - \
        image_draw.textlength(fullname, fullname_font)

    first_name_font = get_image_font(60)
    first_name_position = image.width - \
        image_draw.textlength(first_name, first_name_font)

    last_name_font = get_image_font(60)
    last_name_position = image.width - \
        image_draw.textlength(last_name, last_name_font)

    # image_draw.text(
    #     (fullname_position / 2, 1000 - offset),
    #     fullname,
    #     fill='#002757',
    #     font=fullname_font,
    #     stroke_width=3,
    #     stroke_fill='#002757'
    # )

    image_draw.text(
        (first_name_position / 2, 1000 - offset),
        first_name,
        fill='#002757',
        font=first_name_font,
        stroke_width=2,
        stroke_fill='#002757'
    )

    image_draw.text(
        (last_name_position / 2, 1067 - offset),
        last_name,
        fill='#002757',
        font=last_name_font,
        stroke_width=2,
        stroke_fill='#002757'
    )

    # Draw type box and title
    type_height = 200
    type_box = Image.new('RGBA', (image.width, type_height), data['color'])
    type_box_draw = ImageDraw.Draw(type_box)

    type_title_font_size = 60
    type_title_font = get_image_font(type_title_font_size)
    type_title_with = type_box.width - \
        type_box_draw.textlength(data['type'], type_title_font)

    type_box_draw.text(
        (type_title_with / 2, ((type_height - type_title_font_size - 15) / 2)),
        data['type'],
        fill=data['text_color'],
        font=type_title_font,
        stroke_width=2,
        stroke_fill=data['text_color']
    )

    image.paste(type_box, (0, image.height - 200))

    # Draw Temp Image QR code
    qr_size = (225, 225)
    qr_position = int((image.width - qr_size[0]) / 2), 1140 - offset

    image_copy = image.copy()
    qr_found_data_image = get_qr_code(
        f'{settings.FRONTEND_DETAIL_URL}/404', qr_size)
    image_copy.paste(qr_found_data_image, qr_position)

    # Draw QR Code
    qr_data = f'{
        settings.FRONTEND_DETAIL_URL}/{data['accreditation']}/{data['pk']}/?uuid={data['uuid']}'
    qr_image = get_qr_code(qr_data, qr_size)
    image.paste(qr_image, qr_position)

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

    # Obtener la fecha y hora actual en el formato YYYYMMDD_HH
    today_date_time = datetime.today().strftime('%Y%m%d_%H')

    # Generar la ruta base para guardar los archivos
    base_save_path = (
        settings.BASE_DIR /
        'certifications' /
        accreditation /
        country
    )
    base_save_path.mkdir(parents=True, exist_ok=True)

    # Generar la ruta completa con fecha y hora sin minutos ni segundos
    save_path = (
        base_save_path /
        today_date_time /
        str(data['type']).replace(' ', '_').lower()
    )

    # Crear la carpeta si no existe
    if not save_path.exists():
        save_path.mkdir(parents=True)

    # Generar el nombre del archivo
    filename = f'{data["type"]} {data["fullname"]}'.replace(' ', '_').lower()

    # Guardar la imagen PDF
    image.save(save_path / f'{filename}.pdf')

    # Actualizar el objeto item con los datos necesarios
    item.uuid = data['uuid']
    item.certificated = True

    # Guardar la imagen PNG en bytes
    image_bytes = BytesIO()
    image_copy.save(image_bytes, format='PNG')
    image_bytes.seek(0)

    # Guardar la imagen PNG en el objeto item
    item.certification.save(f'{filename}.png', image_bytes, save=False)
    item.save()


def draw_overflight_permission(pk: int):
    def draw_flight_type(flightType: str):
        if flightType == Aircfraft.FlightType.FLIGHT:
            return (1210, 785)
        else:
            return (1210, 850)

    def draw_aircraft_type(aircraftType: str):
        if aircraftType == Aircfraft.AircraftType.EMERGENCY:
            return (450, 1020)
        elif aircraftType == Aircfraft.AircraftType.AMBULANCE:
            return (832, 1020)
        elif aircraftType == Aircfraft.AircraftType.CHARTER:
            return (1125, 1020)
        elif aircraftType == Aircfraft.AircraftType.MILITARY:
            return (1400, 1020)
        elif aircraftType == Aircfraft.AircraftType.TECHNICAL_SCALE:
            return (2325, 1020)
        else:
            return (0, 0)

    def draw_category(category: str):
        if category == Aircfraft.Category.TECHNICIANS:
            return (379, 2010)
        elif category == Aircfraft.Category.DIPLOMATS:
            return (800, 2010)
        elif category == Aircfraft.Category.MILITARIES:
            return (1170, 2010)
        elif category == Aircfraft.Category.RESCUERS:
            return (1955, 2010)
        elif category == Aircfraft.Category.VOLUNTEERS:
            return (1580, 2010)
        else:
            return (0, 0)

    data: Aircfraft = Aircfraft.objects.get(pk=pk)

    template = (settings.BASE_DIR / 'credentials' /
                'static' / 'credentials' / 'overflight_permission.jpg')

    image = Image.open(template)
    image_draw = ImageDraw.Draw(image)

    # Draw Date
    image_draw.text((320, 605), data.created_at.date().strftime('%Y-%m-%d'), fill='black',
                    font=ImageFont.load_default(42))

    # Draw Applicant
    image_draw.text((410, 720), data.created_by.get_full_name(), fill='black',
                    font=ImageFont.load_default(42))

    # Draw applicant
    image_draw.text((1830, 720), data.country.name, fill='black',
                    font=ImageFont.load_default(42))

    image_draw.text(draw_flight_type(data.flight_type), 'X', fill='black',
                    font=ImageFont.load_default(42))

    image_draw.text(draw_aircraft_type(data.aircraft_type), 'X',
                    fill='black', font=ImageFont.load_default(42))

    image_draw.text((550, 1360), data.arrival_date.strftime(
        '%Y-%m-%d'), fill='black', font=ImageFont.load_default(40))

    image_draw.text((930, 1360), data.arrival_date.time().strftime(
        '%H:%M'), fill='black', font=ImageFont.load_default(42))

    # flight procedence
    image_draw.text((1700, 1360), data.origin, fill='black',
                    font=ImageFont.load_default(42))

    # flight model
    image_draw.text((650, 1472), data.model, fill='black',
                    font=ImageFont.load_default(42))

    # flight registration
    image_draw.text((1360, 1472), data.registration, fill='black',
                    font=ImageFont.load_default(42))

    # draw aircraft type
    image_draw.text((2050, 1472), data.get_aircraft_type_display(), fill='black',
                    font=ImageFont.load_default(42))

    # draw aircraft call sign
    image_draw.text((560, 1590), data.call_sign, fill='black',
                    font=ImageFont.load_default(42))

    image_draw.text((520, 1710), data.ground_facilities,
                    fill='black', font=ImageFont.load_default(42))

    image_draw.text((670, 1830), str(data.passengers_count), fill='black',
                    font=ImageFont.load_default(42))

    image_draw.text((2000, 1830), data.destination, fill='black',
                    font=ImageFont.load_default(42))

    image_draw.text(draw_category(data.category), 'X',
                    fill='black', font=ImageFont.load_default(42))

    image.save('aircraft.pdf')


def get_vehicle_certification(item: GeneralVehicle) -> tuple[Image, Image]:
    template = settings.BASE_DIR / 'credentials' / \
        'static' / 'credentials' / 'permisoVehicularV002.jpg'

    image = Image.open(template)
    draw = ImageDraw.Draw(image)

    # Draw title
    title = f'{item.pk:0>3}'
    title_font = get_image_font(450)
    title_position = (image.width - draw.textlength(title, title_font))

    draw.text(
        (title_position / 2, 1250),
        title,
        fill='#002757',
        font=title_font,
        stroke_width=3,
        stroke_fill='#002757'
    )

    # Draw Color
    # type_width = 1415
    # type_height = 407
    # type_box = Image.new(
    #     'RGBA',
    #     (type_width, type_height),
    #     item.certification_information.color,
    # )

    # image.paste(type_box, (235, image.height - 625))

    # Draw Temp Image QR code
    qr_position = int(image.width - 570), int(image.height - 660)

    image_copy = image.copy()
    qr_found_data_image = get_qr_code(
        f'{settings.FRONTEND_DETAIL_URL}/404', (435, 435))
    image_copy.paste(qr_found_data_image, qr_position)

    # Draw QR Code
    qr_data = f'{
        settings.FRONTEND_DETAIL_URL}/general-vehicles/{item.pk}/?uuid={item.uuid}'
    qr_image = get_qr_code(qr_data, (435, 435))
    image.paste(qr_image, qr_position)

    return image, image_copy


def certificate_vehicle_accreditation(item: GeneralVehicle):
    item.uuid = str(uuid4()).split('-')[0].upper()

    data = get_vehicle_certification(item)
    image, image_copy = data

    save_path = (
        settings.BASE_DIR /
        'certifications' /
        'vehicles'
    )

    if not save_path.exists():
        save_path.mkdir(parents=True)

    filename = str(item.vehicle.plate)
    image.save(save_path / f'{filename}.pdf')

    item.certificated = True

    image_bytes = BytesIO()
    image_copy.save(image_bytes, format='PNG')
    image_bytes.seek(0)

    item.certification.save(f'{filename}.png', image_bytes, save=False)
    item.save()


def get_credential(item: models.Model, template: str, filename, folder_name):
    item.uuid = str(uuid4()).split('-')[0].upper()

    doc = DocxTemplate(template)
    jinja_env = jinja2.Environment()

    save_path = (
        settings.BASE_DIR /
        'certifications' /
        folder_name
    )

    if not save_path.exists():
        save_path.mkdir(parents=True)

    context = {
        'data': item,
    }

    doc.render(context, jinja_env)
    doc.save(save_path / f'{filename}.docx')

    convert_docx_to_pdf(rf'{save_path / f'{filename}.docx'}')

    item.certificated = True
    file_path = save_path / f'{filename}.pdf'
    file = File(file=open(file_path, 'rb'), name=f'{filename}.pdf')

    if os.path.exists(f'{save_path / filename}.docx'):
        os.remove(f'{save_path / filename}.docx')

    item.certification.save(name=f'{filename}.pdf', content=file, save=False)
    item.save()
