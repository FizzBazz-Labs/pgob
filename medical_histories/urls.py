from django.urls import path

from medical_histories.views import MedicalHistoryListApiView

app_name = 'medical_histories'

urlpatterns = [
    path('medical_histories/',
         MedicalHistoryListApiView.as_view(), name='list-create'),
]
