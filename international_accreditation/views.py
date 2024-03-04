from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from international_accreditation.models import InternationalAccreditation

from international_accreditation.serializers import InternationalAccreditationSerializer, InternationalAccreditationReadSerializer, InternationalAccreditationUpdateSerializer

from rest_framework.permissions import IsAuthenticated


class InternationalListCreateApiView(ListCreateAPIView):
    queryset = InternationalAccreditation.objects.all()
    serializer_class = InternationalAccreditationSerializer
    permission_classes = [IsAuthenticated]

class InternationalRetrieveApiView(RetrieveUpdateAPIView):
    queryset = InternationalAccreditation.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return InternationalAccreditationUpdateSerializer
        return InternationalAccreditationReadSerializer    
    permission_classes = [IsAuthenticated]
