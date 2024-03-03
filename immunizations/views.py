from django.shortcuts import render

from rest_framework.generics import ListAPIView

from immunizations.models import Immunization

from immunizations.serializers import ImmunizationSerializer

class ImmunizationsListApiView(ListAPIView):
    queryset = Immunization.objects.all()
    serializer_class = ImmunizationSerializer