from django.urls import path


from overflight_non_commercial_aircraft.views import OverflightNonCommercialAircraftCreateApiView, OverflightNonCommercialAircraftRetrieveApiView

urlpatterns = [
    path('overflight-non-commercial-aircraft/',
         OverflightNonCommercialAircraftCreateApiView.as_view(),
         name='overflight-non-commercial-aircraft-create'),
    path('overflight-non-commercial-aircraft/<int:pk>/',
         OverflightNonCommercialAircraftRetrieveApiView.as_view(), name='overflight-non-commercial-aircraft-detail')
]
