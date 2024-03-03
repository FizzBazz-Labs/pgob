from django.urls import path

from positions.views import PositionsListApiView

app_name = 'positions'

urlpatterns = [
    path('positions/',
         PositionsListApiView.as_view(), name='list-create'),
]
