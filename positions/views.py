from django.shortcuts import render

from rest_framework.generics import ListAPIView

from positions.models import Position

from positions.serializers import PositionSerializer


class PositionsListApiView(ListAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    pagination_class = None
