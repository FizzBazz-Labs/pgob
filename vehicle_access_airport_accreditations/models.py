from django.db import models
from django.contrib.auth import get_user_model

from core.models import AccreditationStatus

from accreditations.models import Accreditation


class VehicleAccessAirportAccreditations(Accreditation):
    country = models.ForeignKey('countries.Country', on_delete=models.CASCADE,
                                related_name='vehicle_access_airport_accreditations')
    information_responsible = models.CharField(max_length=150)
    vehicles = models.ManyToManyField(
        'vehicles.Vehicle', related_name='vehicle_access_airport_accreditations')
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='vehicle_access_airport_accreditations')

    reviewed_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='vehicle_airport_access_reviewed_set')
    reviewed_comment = models.TextField(blank=True)

    authorized_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='vehicle_airport_access_authorized_set')

    rejected_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='vehicle_airport_access_rejected_set')

    status = models.CharField(
        max_length=150,
        choices=AccreditationStatus.choices,
        default=AccreditationStatus.PENDING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.country.name} - {self.information_responsible}'
