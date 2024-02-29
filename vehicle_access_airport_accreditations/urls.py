from django.urls import path

from vehicle_access_airport_accreditations.views import VehicleAccessAirportAccreditationsListApiView, VehicleAccessAirportAccreditationsRetrieveApiView

app_name = 'vehicle_access_airport_accreditations'

urlpatterns = [
    path('vehicle_access_airport-accreditations/',
         VehicleAccessAirportAccreditationsListApiView.as_view(), name='list-create'),
    path('vehicle_access_airport-accreditations/<int:pk>/',
         VehicleAccessAirportAccreditationsRetrieveApiView.as_view(), name='detail'),
]
