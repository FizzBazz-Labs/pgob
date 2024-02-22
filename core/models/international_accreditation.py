from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


def image_filename(instance, filename: str):
    filename = filename.lower().replace(' ', '').replace('-', '')
    return f'internationals/{instance.first_name}_{instance.last_name}/{filename}'


def authorization_letter_filename(instance, filename: str):
    return f'internationals/{instance.first_name}_{instance.last_name}/authorizations/{filename}'


class InternationalAccreditation(models.Model):
    class AccreditationType(models.TextChoices):
        OFFICIAL_DELEGATION_HEAD = (
            'jefe_de_delegación_oficial',
            _('Jefe de Delegación Oficial'),
        )
        OFFICIAL_DELEGATION = 'delegación_oficial', _('Delegación Oficial')
        PROTOCOL = 'protocolo', _('Protocolo')
        SECURITY = 'seguridad', _('Seguridad')
        SUPPORT_STAFF = 'personal_de_apoyo', _('Personal de Apoyo')
        OFFICIAL_PRESS = 'prensa_oficial', _('Prensa Oficial')
        CREW = 'tripulación', _('Tripulación')
        COMMERCIAL_NEWSLETTER = 'prensa_comercial', _('Prensa Comercial')

    country = models.ForeignKey(
        'countries.Country',
        on_delete=models.PROTECT,
        related_name='international_forms')

    # Personal Data
    image = models.ImageField(upload_to=image_filename)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    passport_id = models.CharField(max_length=150)

    position = models.ForeignKey(
        'positions.Position',
        on_delete=models.PROTECT,
        related_name='international_forms')
    sub_position = models.ForeignKey(
        'positions.SubPosition',
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='international_forms')
    media_channel = models.ForeignKey(
        'media_channels.MediaChannel',
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='international_forms')
    authorization_letter = models.FileField(
        upload_to=authorization_letter_filename,
        blank=True)

    institution = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=150)
    phone_number_2 = models.CharField(max_length=150)
    email = models.EmailField()
    birthday = models.DateField()
    birthplace = models.CharField(max_length=150)

    # Medical Information
    blood_group = models.CharField(max_length=150, blank=True)
    blood_rh_factor = models.CharField(max_length=150, blank=True)
    age = models.PositiveIntegerField(default=18)
    diseases = models.TextField()
    medication_1 = models.CharField(max_length=200, blank=True)
    medication_2 = models.CharField(max_length=200, blank=True)
    medication_3 = models.CharField(max_length=200, blank=True)
    medication_4 = models.CharField(max_length=200, blank=True)
    allergies = models.ManyToManyField(
        'allergies.Allergy',
        related_name='international_forms',
        blank=True)
    immunizations = models.ManyToManyField(
        'immunizations.Immunization',
        related_name='international_forms',
        blank=True)
    medicals = models.ManyToManyField(
        'medical_histories.MedicalHistory',
        related_name='international_forms',
        blank=True)
    surgical = models.CharField(max_length=150, blank=True)
    doctor_name = models.CharField(max_length=100, blank=True)

    # Hotel Information
    hotel_name = models.CharField(max_length=120)
    hotel_address = models.CharField(max_length=120)
    hotel_phone = models.CharField(max_length=120)

    # Flight Information
    flight_arrival_date = models.DateField()
    flight_arrival_time = models.TimeField()
    flight_arrival_number = models.CharField(max_length=150)
    flight_from = models.ForeignKey(
        'countries.Country',
        on_delete=models.PROTECT,
        related_name='flight_from')

    flight_departure_date = models.DateField()
    flight_departure_time = models.TimeField()
    flight_departure_number = models.CharField(max_length=150)
    flight_to = models.ForeignKey(
        'countries.Country',
        on_delete=models.PROTECT,
        related_name='flight_to')

    # Accreditation Type
    type = models.CharField(max_length=150, choices=AccreditationType.choices)

    authorized_by = models.CharField(max_length=150, blank=True)
    authorized_by_position = models.ForeignKey(
        'positions.Position',
        on_delete=models.PROTECT)

    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='international_forms')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
