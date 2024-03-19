from django.urls import path

from vehicles.views import VehicleCreateView

urlpatterns = [
    path('vehicles/', VehicleCreateView.as_view(), name='vehicles'),
]
