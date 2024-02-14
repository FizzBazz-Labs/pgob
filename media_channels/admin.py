from django.contrib import admin

from media_channels.models import MediaChannel


@admin.register(MediaChannel)
class MediaChannelAdmin(admin.ModelAdmin):
    ...
