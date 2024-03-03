from django.urls import path

from international_accreditation.views import InternationalListCreateApiView, InternationalRetrieveApiView

app_name = 'international_accreditation'

urlpatterns = [
    path('international-accreditations/',
         InternationalListCreateApiView.as_view(), name='list-create'),
    path('international-accreditations/<int:pk>/',
         InternationalRetrieveApiView.as_view(), name='detail'),
]
