from rest_framework import serializers

from media_channels.models import MediaChannel


class MediaChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaChannel
        fields = ['id', 'name']
