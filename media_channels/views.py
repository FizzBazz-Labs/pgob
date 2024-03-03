from django.shortcuts import render

from rest_framework.generics import ListAPIView

from media_channels.models import MediaChannel

from media_channels.serializers import MediaChannelSerializer

class MediaChannelListApiView(ListAPIView):
    queryset = MediaChannel.objects.all()
    serializer_class = MediaChannelSerializer