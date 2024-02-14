from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _


def image_filename(self, filename: str):
    filename = filename.lower().replace(' ', '').replace('-', '')
    return f'nationals/{self.first_name}_{self.last_name}/{filename}'


def authorization_letter_filename(instance, filename: str):
    return f'nationals/authorization_letters/{filename}'


class NationalAccreditation(models.Model):
    class AccreditationType(models.TextChoices):
        GENERAL_COORDINATION = (
            'coordinación_general',
            _('Coordinación General'),
        )
        PROTOCOL = 'protocolo', _('Protocolo')
        SECURITY = 'seguridad', _('Seguridad')
        TECHNICAL_STAFF = 'personal_técnico', _('Personal Técnico')
        OFFICIAL_DELEGATION = 'Delegación Oficial', _('Delegación Oficial')
        LINK = 'enlace', _('Enlace')
        SUPPLIER = 'proveedor', _('Proveedor')
        NEWSLETTER_COMMITTEE = 'comisión_de_prensa', _('Comisión de Prensa')
        COMMERCIAL_NEWSLETTER = 'prensa_comercial', _('Prensa Comercial')

    image = models.ImageField(upload_to=image_filename)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    passport_id = models.CharField(max_length=100)
    position = models.ForeignKey(
        'positions.Position',
        on_delete=models.PROTECT,
        related_name='national_forms')
    sub_position = models.ForeignKey(
        'positions.SubPosition',
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='national_forms')
    media_channel = models.ForeignKey(
        'media_channels.MediaChannel',
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='national_forms')
    authorization_letter = models.FileField(
        upload_to=authorization_letter_filename, blank=True)
    institution = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=150)
    phone_number_2 = models.CharField(max_length=150)
    email = models.EmailField()
    birthday = models.DateField()
    birthplace = models.CharField(max_length=250)
    blood_type = models.CharField(max_length=150)

    type = models.CharField(max_length=150, choices=AccreditationType.choices)

    authorized_by = models.CharField(max_length=150)
    # date = models.DateField()

    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='national_forms')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
