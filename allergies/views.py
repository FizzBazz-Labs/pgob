from django.shortcuts import render

from rest_framework.generics import ListAPIView

from allergies.models import Allergy

from allergies.serializers import AllergySerializer

class AllergiesListApiView(ListAPIView):
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer