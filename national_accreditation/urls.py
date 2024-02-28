from django.urls import path

from national_accreditation.views import NationalListCreateApiView, NationalRetrieveApiView

urlpatterns = [
    path('national-accreditations/',
         NationalListCreateApiView.as_view(), name='national-accreditations-create'),
    path('national-accreditations/<int:pk>/',
         NationalRetrieveApiView.as_view(), name='national-accreditations-detail')
    # Add your URL patterns here
]
