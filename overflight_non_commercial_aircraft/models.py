from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import AccreditationStatus


class OverflightNonCommercialAircraft(models.Model):

    class FlightType(models.TextChoices):
        CIVIL = 'CIVIL', _('Civil')
        MILITARY = 'MILITARY', _('Militar')
        EMERGENCY = 'EMERGENCY', _('Emergencia')
        AMBULANCE = 'AMBULANCE', _('Ambulancia')
        CHARTER = 'CHARTER', _('Charter')
        OVERFLIGHT = 'OVERFLIGHT', _('Sobrevuelo')
        TECHNICAL_SCALE = 'TECHNICAL_SCALE', _('Escala Técnica')

    country = models.ForeignKey(
        'countries.Country',
        on_delete=models.PROTECT,
        related_name='flight_forms')

    # Aircraft Information
    aircraft_type = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    flight_type = models.CharField(
        max_length=50,
        choices=FlightType.choices,
        default=FlightType.CIVIL)

    # Fixed Base Operator (FBO) when flight_type is CHARTER
    fbo_attendant = models.CharField(max_length=150, blank=True)

    registration = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    call_sign = models.CharField(max_length=150)
    commander_name = models.CharField(max_length=150)
    crew_members_count = models.IntegerField()
    pmi_name = models.CharField(max_length=150)
    position = models.ForeignKey(
        'positions.Position',
        on_delete=models.PROTECT,
        related_name='flight_forms')
    sub_position = models.ForeignKey(
        'positions.SubPosition',
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='flight_forms')
    passengers_count = models.IntegerField()

    # Flight information
    arrival_date = models.DateField()
    departure_date = models.DateField()
    overflight_info = models.TextField()
    landing_info = models.TextField()
    origin = models.CharField(max_length=150)
    destination = models.CharField(max_length=150)
    route = models.CharField(max_length=150)
    ground_facilities = models.TextField()

    # signature = models.CharField(max_length=150, blank=True, null=True,)

    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='flight_forms')

    reviewed_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='overflight_aircraft_reviewed_set')

    authorized_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='overflight_aircraft_authorized_set')

    rejected_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='overflight_aircraft_rejected_set')

    status = models.CharField(
        max_length=150,
        choices=AccreditationStatus.choices,
        default=AccreditationStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.country} - {self.arrival_date} - {self.aircraft_type} - {self.position.name}'
