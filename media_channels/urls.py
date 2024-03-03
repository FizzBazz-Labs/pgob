from django.urls import path

from media_channels.views import MediaChannelListApiView

app_name = 'media_channels'

urlpatterns = [
    path('media_channels/',
         MediaChannelListApiView.as_view(), name='list-create'),
]
