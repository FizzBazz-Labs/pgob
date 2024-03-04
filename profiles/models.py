
from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        related_name='profile',
        on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    country = models.ForeignKey(
        'countries.Country',
        on_delete=models.CASCADE,
        related_name='profiles')
    passport_id = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.user.username
