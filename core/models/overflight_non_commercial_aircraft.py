from django.db import models
from django.utils.translation import gettext as _


class OverflightNonCommercialAircraft(models.Model):

    def upload_file_name(self, filename):
        return f'fligth_request/{self.accreditation_type}/{filename}'

    def create_image_path(self, filename: str):
        filename = filename.lower().replace(' ', '').replace('-', '')

        return f'fligth_request/{self.id}/{filename}'

    class CivilianMilitary(models.TextChoices):
        CIVIL = 'Civil', _('Civil')
        MILITARY = 'Military', _('Military')

    country = models.ForeignKey('countries.Country', on_delete=models.CASCADE)

    aircraft_type = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    civilian_military = models.CharField(
        max_length=50, choices=CivilianMilitary.choices)
    registration_number = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    call_sign = models.CharField(max_length=150)
    commander_name = models.CharField(max_length=150)
    crew_members_count = models.IntegerField()
    pmi_name = models.CharField(max_length=150)
    passengers_count = models.IntegerField()

    # Positions
    position = models.ForeignKey(
        'positions.Position',
        on_delete=models.PROTECT,
        related_name='flight_forms')
    sub_position = models.ForeignKey(
        'positions.SubPosition',
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='flight_forms')

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
    # PEDIR UNA FIRMA DIGITAL
    # PREGUNTAR COMO QUIEREN AGARRAR LA
    request_date = models.DateField()
    requester_signature = models.CharField(max_length=150)
