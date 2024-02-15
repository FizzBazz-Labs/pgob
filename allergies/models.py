from django.db import models


class Allergy(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name
