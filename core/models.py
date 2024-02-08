from django.db import models
from django.utils.translation import gettext as _

class Nationality(models.Model):
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    

class Position(models.Model):
    name = models.CharField(max_length=150)
    
    
class MediaChannel(models.Model):
    name = models.CharField(max_length=120)


class NationalAcreditation(models.Model):
    
    def upload_file_name(self, filename):
        return f'national_accreditation/{self.accreditation_type}/{filename}'
    
    class AccreditationType(models.TextChoices):
        GENERAL_COORDINATION = 'Coordinacion General', _('Coordinacion General')
        PROTOCOL = 'Protocolo', _('Protocolo')
        SECURITY = 'Seguridad', _('Seguridad')
        TECHNICAL_STAFF = 'Personal tecnico', _('Personal tecnico')
        OFFICIAL_DELEGATION = 'Delegacion Oficial', _('Delegacion Oficial')
        LINK = 'Enlace', _('Enlace')
        SUPPLIER = 'Proveedor', _('Proveedor')
        PRESS_COMMITTEE = 'Comision de Prensa', _('Comision de Prensa')
        COMERCIAL_PRESS = 'Prensa Comercial', _('Prensa Comercial')
    
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to=create_file_path(is_image=True))
    last_name = models.CharField(max_length=150)
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, related_name='national_accreditations')
    passport_id = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='national_acreditation')
    letter_of_authorization = models.FileField(upload_to=create_file_path)
    media_channel = models.ForeignKey(MediaChannel, on_delete=models.CASCADE, related_name='national_acreditation')
    institution = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    cellphone = models.CharField(max_length=120)
    email = models.EmailField()
    birthday = models.DateField()
    birthplace = models.CharField(max_length=150)
    blood_type = models.CharField(max_length=150)
    accreditation_type = models.CharField(max_length=120, choices=AccreditationType.choices)
    authorized_by = models.CharField(max_length=150, null=True)
    date = models.DateField()


class InternationalAccreditation(models.Model):
    
    def upload_file_name(self, filename):
        return f'international_accreditation/{self.accreditation_type}/{filename}'
    
    class Allergies(models.TextChoices):
        ENVIRONMENTAL = 'Ambientales', _('Ambientales')
        NUTRITIONAL = 'Alimenticias', _('Alimenticias')
        ANALGESICS = 'Analgesicos', _('Analgesicos')
        ANTIBIOTICS = 'Antibioticos', _('Antibioticos')
        
        
    class Inmunizations(models.TextChoices):
        CONTRAST_CHANNELS = 'Medios de contraste', _('Medios de contraste')
        TETANO = 'Tetano', _('Tetano')
        HEPATITIS = 'Hepatitis', _('Hepatitis')
        OTHERS = 'Otros', _('Otros')
        
    class MEDICAL_HISTORIES(models.TextChoices):
        ISCHEMIC_HEART_DISEASE = 'Cardiopatia Isquemica', _('Cardiopatia Isquemica')
        MYOCARDIAL_INFARCTION = 'Infarto del miocardio', _('Infarto del miocardio')
        ULTIMATE_PACEMAKER = 'Marcapaso definitivo', _('Marcapaso definitivo')
        ANGINA = 'Angina', _('Angina')
        DIABETES_MELLITUS = 'Diabetes Mellitus', _('Diabetes Mellitus')
        ARTERIAL_HYPERTENSION = 'Hipertension arterial', _('Hipertension arterial')
        ARRHYTHMIA = 'Arritmias', _('Arritmia')
        OTHERS = 'Otros', _('Otros')
        
    class AccreditationType(models.TextChoices):
        OFFICIAL_DELEGATION_HEAD = 'Jefe de delegacion oficial', _('jefe de delegacion oficial')
        OFFICIAL_DELEGATION = 'Delegacion Oficial', _('Delegacion Oficial')
        PROTOCOL = 'Protocolo', _('Protocolo')
        SECURITY = 'Seguridad', _('Seguridad')
        SUPPORT_STAFF = 'Personal de apoyo', _('Personal de apoyo')
        OFFICIAL_PRESS = 'Prensa oficial', _('Prensa oficial')
        TRIPULATION = 'Tripulacion', _('Tripulacion')
        COMERCIAL_PRESS = 'Prensa Comercial', _('Prensa Comercial')
    
    country_of_origin = models.ForeignKey(Nationality, on_deleted=models.PROTECT, related_name='international_accreditations')
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to=create_file_path(is_image=True))
    last_name = models.CharField(max_length=150)
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, related_name='international_accreditations')
    passport_id = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='international_accreditations')
    letter_of_authorization = models.FileField(upload_to=create_file_path)
    media_channel = models.ForeignKey(MediaChannel, on_delete=models.CASCADE, related_name='international_accreditations')
    institution = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    cellphone = models.CharField(max_length=120)
    email = models.EmailField()
    birthday = models.DateField()
    birthplace = models.CharField(max_length=150)
    authorized_by = models.CharField(max_length=150, null=True)
    date = models.DateField()
    accreditation_type = models.CharField(max_length=120, choices=AccreditationType.choices)
    # Medical Information
    blood_type = models.CharField(max_length=150)
    age = models.PositiveIntegerField(default=18)
    diseases_under_treatment = models.CharField(max_length=150)
    medications_in_use = models.CharField(max_length=200)
    have_allergies = models.BooleanField(default=True)
    allergies = models.CharField(max_length=100, choices=Allergies.choices, blank=True)
    has_inmunizations = models.BooleanField(default=False)
    immunizations = models.CharField(max_length=120, choices=Inmunizations.choices, blank=True)
    have_medical_history = models.BooleanField(default=False)
    medical_histories = models.CharField(max_length=150, choices=MEDICAL_HISTORIES.choices, blank=True)
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



class SecurityAccreditation(models.Model):
    
    class WeaponType(models.TextChoices):
        PISTOL = 'Pistol', _('Pistol')
        RIFLE = 'Rifle', _('Rifle')
        SHOTGUN = 'Shotgun', _('Shotgun')
        OTHER = 'Other', _('Other')

    class CommunicationType(models.TextChoices):
        RADIO = 'Radio', _('Radio')
        OTHER = 'Other', _('Other')

    date_control = models.DateField()
    time_control = models.TimeField()
    disclaimer_accepted = models.BooleanField(default=False)
    
    # Weapon data
    weapon = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    weapon_type = models.CharField(max_length=50, choices=WeaponType.choices)
    serial_number = models.CharField(max_length=150)
    caliber = models.CharField(max_length=150)
    magazine_quantity = models.IntegerField()
    ammunition_quantity = models.IntegerField()

    # Communication equipment data
    communication_radio = models.CharField(max_length=150)
    communication_model = models.CharField(max_length=150)
    communication_type = models.CharField(max_length=50, choices=CommunicationType.choices)
    communication_serial = models.CharField(max_length=150)
    communication_frequency = models.CharField(max_length=150)
    

class FlightRequest(models.Model):
    class CivilianMilitary(models.TextChoices):
        CIVIL = 'Civil', _('Civil')
        MILITARY = 'Military', _('Military')

    country = models.CharField(max_length=150)
    
    # Aircraft data
    aircraft_type = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    civilian_military = models.CharField(max_length=50, choices=CivilianMilitary.choices)
    registration_number = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    call_sign = models.CharField(max_length=150)
    commander_name = models.CharField(max_length=150)
    crew_members_count = models.IntegerField()
    pmi_name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    passengers_count = models.IntegerField()

    # Flight information
    entry_date = models.DateField()
    exit_date = models.DateField()
    overflight_info = models.TextField()
    landing_info = models.TextField()
    origin = models.CharField(max_length=150)
    destination = models.CharField(max_length=150)
    route = models.CharField(max_length=150)
    ground_facilities = models.TextField()

    # signature and dates
    request_date = models.DateField()
    requester_signature = models.CharField(max_length=150)



class VehicleAccreditation(models.Model):
    country_name = models.CharField(max_length=150)

    class Vehicle(models.Model):

        class VehicleTypes(models.TextChoices):
            CAR = 'Car', _('Car')
            PICK_UP = 'Pick up', _('Pick up')
            VAN = 'Van', _('Van')
            TRUCK = 'Truck', _('Truck')
            OTHER = 'Other', _('Other')

        vehicle_type = models.CharField(max_length=50, choices=VehicleTypes.choices)
        brand = models.CharField(max_length=150)
        color = models.CharField(max_length=150)
        license_plate = models.CharField(max_length=20)
        driver_name = models.CharField(max_length=150)
        driver_id = models.CharField(max_length=20)
        driver_phone = models.CharField(max_length=20)


    vehicles = models.ManyToManyField(Vehicle, related_name='accreditations')

    responsible_info = models.CharField(max_length=150)
    responsible_signatures = models.TextField()
    date = models.DateField()



class CommunicationEquipmentDeclaration(models.Model):
    country_name = models.CharField(max_length=150)
    institution_or_media = models.CharField(max_length=150)

class EquipmentItem(models.Model):
    declaration = models.ForeignKey(CommunicationEquipmentDeclaration, on_delete=models.CASCADE, related_name='items')
    object_type = models.CharField(max_length=50)
    brand = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    serial_number = models.CharField(max_length=150)
    approximate_value = models.DecimalField(max_digits=10, decimal_places=2)





class GeneralVehicleAccreditation(models.Model):
    
    mission = models.TextField()
    vehicle_brand = models.CharField(max_length=150)
    license_plate = models.CharField(max_length=20)
    color = models.CharField(max_length=150)
    driver_name = models.CharField(max_length=150)
    dip = models.CharField(max_length=150)
    assigned = models.TextField()
    
    distinctive = models.TextChoices(max_length=150)
    observations = models.TextField()

    responsible_signatures = models.TextField()
    date = models.DateField()





