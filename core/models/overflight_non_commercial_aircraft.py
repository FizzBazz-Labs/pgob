# from django.contrib.auth import get_user_model
# from django.db import models
# from django.utils.translation import gettext_lazy as _


# class OverflightNonCommercialAircraft(models.Model):

#     class Jurisdiction(models.TextChoices):
#         CIVIL = 'civil', _('Civil')
#         MILITARY = 'military', _('Militar')

#     country = models.ForeignKey(
#         'countries.Country',
#         on_delete=models.PROTECT,
#         related_name='flight_forms')

#     # Aircraft Information
#     aircraft_type = models.CharField(max_length=150)
#     model = models.CharField(max_length=150)
#     jurisdiction = models.CharField(
#         max_length=50,
#         choices=Jurisdiction.choices,
#         default=Jurisdiction.CIVIL)
#     registration = models.CharField(max_length=150)
#     color = models.CharField(max_length=150)
#     call_sign = models.CharField(max_length=150)
#     commander_name = models.CharField(max_length=150)
#     crew_members_count = models.IntegerField()
#     pmi_name = models.CharField(max_length=150)
#     position = models.ForeignKey(
#         'positions.Position',
#         on_delete=models.PROTECT,
#         related_name='flight_forms')
#     sub_position = models.ForeignKey(
#         'positions.SubPosition',
#         on_delete=models.PROTECT,
#         blank=True, null=True,
#         related_name='flight_forms')
#     passengers_count = models.IntegerField()

#     # Flight information
#     arrival_date = models.DateField()
#     departure_date = models.DateField()
#     overflight_info = models.TextField()
#     landing_info = models.TextField()
#     origin = models.CharField(max_length=150)
#     destination = models.CharField(max_length=150)
#     route = models.CharField(max_length=150)
#     ground_facilities = models.TextField()

#     date = models.DateField()
#     signature = models.CharField(max_length=150)

#     created_by = models.ForeignKey(
#         get_user_model(),
#         on_delete=models.PROTECT,
#         related_name='flight_forms')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
