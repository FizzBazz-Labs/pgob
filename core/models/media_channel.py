from django.db import models


class MediaChannel(models.Model):
    name = models.CharField(max_length=120)
