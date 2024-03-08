from django.urls import path

from vehicle_access_airport_accreditations.views import (
    VehicleAccessAirportAccreditationsListCreateApiView, 
    VehicleAccessAirportAccreditationsRetrieveApiView,
    RejectAccreditation, 
    ApproveAccreditation, 
    ReviewAccreditation
)

urlpatterns = [
    path('', VehicleAccessAirportAccreditationsListCreateApiView.as_view()),
    path('<int:pk>/', VehicleAccessAirportAccreditationsRetrieveApiView.as_view()),
    path('<int:pk>/review/', ReviewAccreditation.as_view()),
    path('<int:pk>/approve/', ApproveAccreditation.as_view()),
    path('<int:pk>/reject/', RejectAccreditation.as_view()),
]
