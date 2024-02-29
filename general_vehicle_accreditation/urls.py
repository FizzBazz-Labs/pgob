from django.urls import path

from general_vehicle_accreditation.views import GeneralVehicleAccreditationListApiView, GeneralVehicleAccreditationRetrieveApiView

app_name = 'general_vehicle_accreditation'

urlpatterns = [
    path('general_vehicle_accreditation/',
         GeneralVehicleAccreditationListApiView.as_view(), name='list-create'),
    path('general_vehicle_accreditation/<int:pk>/',
         GeneralVehicleAccreditationRetrieveApiView.as_view(), name='detail'),
]
