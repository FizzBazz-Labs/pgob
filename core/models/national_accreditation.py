from django.db import models
from django.utils.translation import gettext as _

from core.models.media_channel import MediaChannel


class NationalAccreditation(models.Model):

    def upload_file_name(self, filename):
        return f'national_accreditation/{self.accreditation_type}/{filename}'

    def create_image_path(self, filename: str):
        filename = filename.lower().replace(' ', '').replace('-', '')

        return f'national_accreditation/{self.id}/{filename}'

    class AccreditationType(models.TextChoices):
        GENERAL_COORDINATION = 'Coordinacion General', _(
            'Coordinacion General')
        PROTOCOL = 'Protocolo', _('Protocolo')
        SECURITY = 'Seguridad', _('Seguridad')
        TECHNICAL_STAFF = 'Personal tecnico', _('Personal tecnico')
        OFFICIAL_DELEGATION = 'Delegacion Oficial', _('Delegacion Oficial')
        LINK = 'Enlace', _('Enlace')
        SUPPLIER = 'Proveedor', _('Proveedor')
        PRESS_COMMITTEE = 'Comision de Prensa', _('Comision de Prensa')
        COMERCIAL_PRESS = 'Prensa Comercial', _('Prensa Comercial')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to=create_image_path)
    last_name = models.CharField(max_length=150)
    passport_id = models.CharField(max_length=100)

    # Positions
    position = models.ForeignKey(
        'positions.Position',
        on_delete=models.PROTECT,
        related_name='national_forms')
    sub_position = models.ForeignKey(
        'positions.SubPosition',
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='national_forms')

    letter_of_authorization = models.FileField(upload_to=upload_file_name)
    media_channel = models.ForeignKey(
        MediaChannel,
        on_delete=models.CASCADE,
        related_name='national_acreditation')
    institution = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    cellphone = models.CharField(max_length=120)
    email = models.EmailField()
    birthday = models.DateField()
    birthplace = models.CharField(max_length=150)
    blood_type = models.CharField(max_length=150)
    accreditation_type = models.CharField(
        max_length=120, choices=AccreditationType.choices)
    authorized_by = models.CharField(max_length=150, null=True)
    date = models.DateField()
