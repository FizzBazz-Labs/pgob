from io import BytesIO

import pandas as pd
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from accreditations.models import Accreditation
from core.utils import split_space
from core.views import AccreditationViewSet

from commerce.models import Commerce, CommerceEmployee
from commerce.serializers import CommerceSerializer, CommerceEmployeeSerializer


class CommerceViewSet(AccreditationViewSet):
    queryset = Commerce.objects.all()
    serializer_class = CommerceSerializer
    filterset_fields = ['status']
    search_fields = ['created_at__date']

    @action(detail=False,
            methods=['get'],
            permission_classes=[AllowAny])
    def export(self, request, *args, **kwargs) -> HttpResponse:
        queryset = Commerce.objects \
            .filter(status=Accreditation.Status.PENDING) \
            .prefetch_related('employees', 'employees__country')

        if not queryset.exists():
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

        buffer = BytesIO()

        values = []

        for commerce in queryset:
            for person in commerce.employees.all():
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


class CommerceEmployeeViewSet(ModelViewSet):
    queryset = CommerceEmployee.objects.all()
    serializer_class = CommerceEmployeeSerializer
    filterset_fields = ['commerce']
    pagination_class = None
