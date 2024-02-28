from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from international_accreditation.models import InternationalAccreditation
from international_accreditation.serializers import InternationalAccreditationSerializer, InternationalAccreditationReadSerializer


class InternationalListCreateApiView(ListCreateAPIView):
    queryset = InternationalAccreditation.objects.all()
    serializer_class = InternationalAccreditationSerializer


class InternationalRetrieveApiView(RetrieveAPIView):
    queryset = InternationalAccreditation.objects.all()
    serializer_class = InternationalAccreditationReadSerializer
