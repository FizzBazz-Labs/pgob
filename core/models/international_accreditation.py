from django.db import models
from django.utils.translation import gettext as _

<<<<<<< HEAD
=======
from core.models.position import Position
>>>>>>> auth
from core.models.media_channel import MediaChannel


class MedicalHistory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Allergy(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Inmunization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class InternationalAccreditation(models.Model):

    def upload_file_name(self, filename):
        return f'international_accreditation/{self.accreditation_type}/{filename}'

    def create_image_path(self, filename: str):
        filename = filename.lower().replace(' ', '').replace('-', '')

        return f'international_accreditation/{self.id}/{filename}'

    # class Allergies(models.TextChoices):
    #     ENVIRONMENTAL = 'Ambientales', _('Ambientales')
    #     NUTRITIONAL = 'Alimenticias', _('Alimenticias')
    #     ANALGESICS = 'Analgesicos', _('Analgesicos')
    #     ANTIBIOTICS = 'Antibioticos', _('Antibioticos')

    # class Inmunizations(models.TextChoices):
    #     CONTRAST_CHANNELS = 'Medios de contraste', _('Medios de contraste')
    #     TETANO = 'Tetano', _('Tetano')
    #     HEPATITIS = 'Hepatitis', _('Hepatitis')
    #     OTHERS = 'Otros', _('Otros')

    # class MEDICAL_HISTORIES(models.TextChoices):
    #     ISCHEMIC_HEART_DISEASE = 'Cardiopatia Isquemica', _('Cardiopatia Isquemica')
    #     MYOCARDIAL_INFARCTION = 'Infarto del miocardio', _('Infarto del miocardio')
    #     ULTIMATE_PACEMAKER = 'Marcapaso definitivo', _('Marcapaso definitivo')
    #     ANGINA = 'Angina', _('Angina')
    #     DIABETES_MELLITUS = 'Diabetes Mellitus', _('Diabetes Mellitus')
    #     ARTERIAL_HYPERTENSION = 'Hipertension arterial', _('Hipertension arterial')
    #     ARRHYTHMIA = 'Arritmias', _('Arritmia')
    #     OTHERS = 'Otros', _('Otros')

    class AccreditationType(models.TextChoices):
        OFFICIAL_DELEGATION_HEAD = 'Jefe de delegacion oficial', _(
            'jefe de delegacion oficial')
        OFFICIAL_DELEGATION = 'Delegacion Oficial', _('Delegacion Oficial')
        PROTOCOL = 'Protocolo', _('Protocolo')
        SECURITY = 'Seguridad', _('Seguridad')
        SUPPORT_STAFF = 'Personal de apoyo', _('Personal de apoyo')
        OFFICIAL_PRESS = 'Prensa oficial', _('Prensa oficial')
        TRIPULATION = 'Tripulacion', _('Tripulacion')
        COMERCIAL_PRESS = 'Prensa Comercial', _('Prensa Comercial')

    country = models.ForeignKey(
        'countries.Country',
        on_delete=models.PROTECT,
        related_name='international_forms')
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to=create_image_path)
    last_name = models.CharField(max_length=150)
    passport_id = models.CharField(max_length=100)

    # Positions
    position = models.ForeignKey(
        'positions.Position',
        on_delete=models.PROTECT,
        related_name='international_forms')
    sub_position = models.ForeignKey(
        'positions.SubPosition',
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='international_forms')

    letter_of_authorization = models.FileField(upload_to=create_image_path)
    media_channel = models.ForeignKey(
        MediaChannel, on_delete=models.CASCADE, related_name='international_accreditations')
    institution = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    cellphone = models.CharField(max_length=120)
    email = models.EmailField()
    birthday = models.DateField()
    birthplace = models.CharField(max_length=150)
    authorized_by = models.CharField(max_length=150, null=True)
    date = models.DateField()
    accreditation_type = models.CharField(
        max_length=120, choices=AccreditationType.choices)
    # Medical Information
    blood_type = models.CharField(max_length=150)
    age = models.PositiveIntegerField(default=18)
    diseases_under_treatment = models.CharField(max_length=150)
    medications_in_use = models.CharField(max_length=200)
    have_allergies = models.BooleanField(default=False)
    allergies = models.ManyToManyField(
        Allergy, related_name='international_accreditations', blank=True)
    has_inmunizations = models.BooleanField(default=False)
    inmunizations = models.ManyToManyField(
        Inmunization, related_name='international_accreditations', blank=True)
    have_medical_history = models.BooleanField(default=False)
    medical_histories = models.ManyToManyField(
        MedicalHistory, related_name='international_accreditations', blank=True)
    surgical_history = models.CharField(max_length=150, blank=True)
    has_personal_doctor = models.BooleanField(default=False)
    doctor_name = models.CharField(max_length=100, blank=True)
    # accomodation information
    hotel_name = models.CharField(max_length=120)
    hotel_address = models.CharField(max_length=120)
    hotel_phone = models.CharField(max_length=120)
    # Flight Information
    flight_arrival_date = models.DateField()
    flight_arrival_time = models.TimeField()
    flight_arrival_number = models.CharField(max_length=120)
    fligth_procedence = models.CharField(max_length=120)
    flight_departure_date = models.DateField()
    flight_departure_time = models.TimeField()
    flight_departure_number = models.CharField(max_length=120)
    flight_destination = models.CharField(max_length=120)
