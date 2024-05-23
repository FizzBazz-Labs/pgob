from django.http import HttpResponse

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from credentials.utils import draw_overflight_permission


from overflight_non_commercial_aircraft.models import OverflightNonCommercialAircraft
from overflight_non_commercial_aircraft.serializers import OverflightNonCommercialAircraftSerializer, \
    OverflightNonCommercialAircraftReadSerializer

from core.views import AccreditationViewSet


class OverflightNonCommercialAircraftViewSet(AccreditationViewSet):
    queryset = OverflightNonCommercialAircraft.objects.all()
    filterset_fields = ['status', 'country']
    search_fields = ['created_at__date']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return OverflightNonCommercialAircraftReadSerializer

        return OverflightNonCommercialAircraftSerializer

    @action(detail=True, methods=['get'])
    def certificate(self, request, pk=None, *args, **kwargs) -> HttpResponse:
        queryset = self.get_queryset()

        try:
            item: OverflightNonCommercialAircraft = queryset.get(pk=pk)
            draw_overflight_permission(item.pk)

            with open('aircraft.pdf', 'rb') as pdf_file:

                response = HttpResponse(
                    pdf_file, content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename=Permiso_Sobrevuelo_{
                    item.country.name}.pdf'

            return response

        except queryset.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
