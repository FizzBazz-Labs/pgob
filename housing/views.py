from io import BytesIO

import pandas as pd
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from accreditations.models import Accreditation
from core.views import AccreditationViewSet
from core.utils import split_space

from housing.models import Housing, HousingPerson
from housing.serializers import HousingSerializer, HousingPersonSerializer


class HousingViewSet(AccreditationViewSet):
    queryset = Housing.objects.all()
    serializer_class = HousingSerializer
    filterset_fields = ['status']
    search_fields = ['created_at__date']

    @action(detail=False,
            methods=['get'],
            permission_classes=[AllowAny])
    def export(self, request, *args, **kwargs) -> HttpResponse:
        queryset = Housing.objects.filter(status=Accreditation.Status.PENDING).prefetch_related('persons',
                                                                                                'persons__country')
        if not queryset.exists():
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

        buffer = BytesIO()

        values = []

        for housing in queryset:
            for person in housing.persons.all():
                values.append({
                    'ID': person.id,
                    'Primer Nombre': split_space(person.first_name)[0],
                    'Segundo Nombre': split_space(person.first_name)[1],
                    'Primer Apellido': split_space(person.last_name)[0],
                    'Segundo Apellido': split_space(person.last_name)[1],
                    'Cédula': person.passport_id,
                    'Fecha de Nacimiento': person.birthday.strftime('%d-%m-%Y'),
                    'Nacionalidad': person.country.nationality
                })

        pd.DataFrame(values).to_excel(buffer, index=False, sheet_name='Personas')
        buffer.seek(0)

        response = HttpResponse(
            buffer.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )

        response['Content-Disposition'] = 'attachment; filename=data.xlsx'

        return response


class HousingPersonViewSet(ModelViewSet):
    queryset = HousingPerson.objects.all()
    serializer_class = HousingPersonSerializer
    filterset_fields = ['housing']
    pagination_class = None
