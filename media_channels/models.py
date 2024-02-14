from django.db import models


class MediaChannel(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name
