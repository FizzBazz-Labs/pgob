from typing import Any
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

import qrcode

from django.conf import settings


def get_certification(data: dict[str, Any]) -> Image:
    template = settings.BASE_DIR / 'credentials' / 'static' / 'credentials' / 'base.png'

    image = Image.open(template)
    image_draw = ImageDraw.Draw(image)

    # Draw title
    title_font = ImageFont.load_default(30)
    title_position = (image.width - image_draw.textlength(data['president'], title_font))

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
    term_date_position = (image.width - image_draw.textlength(data['term_date'], term_date_font))
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
    fullname_position = image.width - image_draw.textlength(data['fullname'], fullname_font)

    image_draw.text(
        (fullname_position / 2, 580),
        data['fullname'],
        fill='#002757',
        font=fullname_font,
        stroke_width=1,
        stroke_fill='#002757'
    )

    # Draw QR code
    qr_data = f'{settings.FRONTEND_DETAIL_URL}/{data['accreditation']}/{data['pk']}/?uuid={data['uuid']}'
    qr_code = qrcode.make(qr_data)
    qr_buffer = BytesIO()
    qr_code.save(qr_buffer, format='PNG')
    qr_buffer.seek(0)

    qr_image = Image.open(qr_buffer).resize((175, 175))

    image.paste(qr_image, (
        int((image.width - 175) / 2),
        780,
    ))

    # Draw type box and title
    type_box = Image.new('RGBA', (image.width - 29, 100), data['color'])
    type_box_draw = ImageDraw.Draw(type_box)

    type_title_font = ImageFont.load_default(30)
    type_title_with = type_box.width - type_box_draw.textlength(data['type'], type_title_font)

    type_box_draw.text(
        (type_title_with / 2, 30),
        data['type'],
        fill=data['text_color'],
        font=type_title_font,
    )

    image.paste(type_box, (19, image.height - 118))

    return image
