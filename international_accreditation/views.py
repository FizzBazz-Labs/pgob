from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from international_accreditation.models import InternationalAccreditation

from international_accreditation.serializers import InternationalAccreditationSerializer, InternationalAccreditationReadSerializer

from rest_framework.permissions import IsAuthenticated


class InternationalListCreateApiView(ListCreateAPIView):
    queryset = InternationalAccreditation.objects.all()
    serializer_class = InternationalAccreditationSerializer
    permission_classes = [IsAuthenticated]

class InternationalRetrieveApiView(RetrieveAPIView):
    queryset = InternationalAccreditation.objects.all()
    serializer_class = InternationalAccreditationReadSerializer
