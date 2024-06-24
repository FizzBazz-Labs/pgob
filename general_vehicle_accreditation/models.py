from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from accreditations.models import Accreditation

from countries.models import Country


class GeneralVehicleAccreditation(Accreditation):
    class AccreditationType(models.TextChoices):
        OFFICIAL_NEWSLETTER = 'OFFICIAL_NEWSLETTER', _('Prensa Oficial')
        NATIONAL_NEWSLETTER = 'COMMERCIAL_NEWSLETTER', _('Prensa Nacional')
        INTERNATIONAL_NEWSLETTER = 'INTERNATIONAL_NEWSLETTER', _('Prensa Internacional')
        DIPLOMATIC_MISSION = 'DIPLOMATIC_MISSION', _('Misión Diplomática')
        MINREX_OFFICIALS = 'MINREX_OFFICIALS', _('Funcionarios MINREX')
        VEHICLES = 'VEHICLES', _('Vehículos')

    class AccreditationTypeVehicle(models.TextChoices):
        INSTITUTIONAL_SUPPORT = 'INSTITUTIONAL_SUPPORT', _('Apoyo Institucional')
        OTHER = 'OTHER', _('Otro')

    accreditation_type = models.CharField(
        max_length=150,
        choices=AccreditationType.choices,
        default=AccreditationType.DIPLOMATIC_MISSION)
    accreditation_type_vehicle = models.CharField(
        max_length=150,
        choices=AccreditationTypeVehicle.choices,
        default=AccreditationTypeVehicle.INSTITUTIONAL_SUPPORT)
    assigned_to = models.CharField(max_length=150)
    vehicle = models.ForeignKey('vehicles.Vehicle', on_delete=models.PROTECT, null=True)
    country = models.ForeignKey(
        'countries.Country',
        on_delete=models.PROTECT,
        default=Country.get_default_pk,
        blank=True)
    distinctive = models.CharField(max_length=150, blank=True)
    observations = models.CharField(max_length=150, blank=True)
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='general_vehicle_created_set')
    reviewed_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='general_vehicle_reviewed_set',
        blank=True, null=True)
    authorized_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='general_vehicle_authorized_set',
        blank=True, null=True)
    rejected_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='general_vehicle_rejected_set',
        blank=True, null=True)

    certification_information = models.ForeignKey(
        'credentials.VehicleCertification',
        on_delete=models.PROTECT,
        blank=True, null=True)

    def __str__(self):
        return f'{self.accreditation_type} {self.country} - {self.assigned_to}'
