from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from national_accreditation.models import NationalAccreditation
from national_accreditation.serializers import NationalSerializer


class NationalListCreateApiView(ListCreateAPIView):
    queryset = NationalAccreditation.objects.all()
    serializer_class = NationalSerializer
    permission_classes = [IsAuthenticated]


class NationalRetrieveApiView(RetrieveAPIView):
    queryset = NationalAccreditation.objects.all()
    serializer_class = NationalSerializer
    # permission_classes = [IsAuthenticated]
