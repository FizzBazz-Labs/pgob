from django.urls import path

from immunizations.views import ImmunizationsListApiView

app_name = 'immunizations'

urlpatterns = [
    path('immunizations/',
         ImmunizationsListApiView.as_view(), name='list-create'),
]
