from django.shortcuts import render

from rest_framework.generics import ListAPIView

from medical_histories.models import MedicalHistory

from medical_histories.serializers import MedicalHistorySerializer


class MedicalHistoryListApiView(ListAPIView):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer
    pagination_class = None
