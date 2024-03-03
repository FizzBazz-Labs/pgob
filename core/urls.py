from django.urls import path

from core.views import *

app_name = 'core'

urlpatterns = [
    # path('', NationalFormView.as_view(), name='national'),
    # path("international-form/", InternationalFormView.as_view(), name="international"),
    # path('overflight-and-non-commercial-aircraft-form',
    #      OverflightAndNonCommercialAircraftFormView.as_view(),
    #      name='overflight'),

    # path('accreditations/',
    #      AccreditationList.as_view(),
    #      name="form-list"),

    # path('accreditations/nationals/<int:pk>/',
    #      NationalDetailView.as_view(),
    #      name='national-detail'),
    # path('accreditations/internationals/<int:pk>/',
    #      InternationalAccreditationDetail.as_view(),
    #      name='international-detail'),
]
