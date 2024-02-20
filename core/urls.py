from django.urls import path

from core.views import *


app_name = 'core'

urlpatterns = [
    path('', NationalFormView.as_view(), name='national'),
    path("international-form/", InternationalFormView.as_view(), name="international"),
    path('overflight-and-non-commercial-aircraft-form',
         OverflightAndNonCommercialAircraftFormView.as_view(),
         name='overflight'),
    path("form-list/", CreatedFormsView.as_view(), name="form-list")

]
