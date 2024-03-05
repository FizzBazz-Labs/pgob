# from rest_framework.generics import
from rest_framework.views import APIView
from rest_framework.response import Response

from core.serializers import AccreditationsSerializer

from international_accreditation.models import InternationalAccreditation
from national_accreditation.models import NationalAccreditation


class AccreditationListView(APIView):

    def get_accreditations(self):
        data = []

        for item in NationalAccreditation.objects.all():
            data.append({
                'id': item.id,
                'first_name': item.first_name,
                'last_name': item.last_name,
                'type': 'national',
                'country': 'Panamá',
                'status': item.status,
                'created_at': item.created_at,
                'updated_at': item.updated_at,
                'created_by': {
                    'id': item.created_by.id,
                    'username': item.created_by.username,
                    'first_name': item.created_by.first_name,
                    'last_name': item.created_by.last_name,
                    'email': item.created_by.email,
                }
            })

        for item in InternationalAccreditation.objects.all():
            data.append({
                'id': item.id,
                'first_name': item.first_name,
                'last_name': item.last_name,
                'type': 'international',
                'country': item.country.name,
                'status': item.status,
                'created_at': item.created_at,
                'updated_at': item.updated_at,
                'created_by': {
                    'id': item.created_by.id,
                    'username': item.created_by.username,
                    'first_name': item.created_by.first_name,
                    'last_name': item.created_by.last_name,
                    'email': item.created_by.email,
                }
            })

        return data

    def get(self, request):
        accreditations = self.get_accreditations()
        accreditations_serializer = AccreditationsSerializer(
            accreditations, many=True)

        return Response({
            'accreditations': accreditations_serializer.data,
        })
