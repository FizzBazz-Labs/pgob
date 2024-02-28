from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from international_accreditation.models import InternationalAccreditation
from national_accreditation.models import NationalAccreditation

class AccreditationListView(APIView):
    def get(self, request):
        international_accreditation = InternationalAccreditation.objects.all()
        national_accreditation = NationalAccreditation.objects.all()


        international_data = [
            {
                "id": item.id,
                "created_at": item.created_at.date(),
                "type": item.type,
                "country": item.country.name,
            }
            for item in international_accreditation
        ]

        national_data = [
            {
                "id": item.id,
                "created_at": item.created_at.date(),
                "type": item.type,
                "country": "Panama",
            }
            for item in national_accreditation
        ]

        accreditations = international_data + national_data

        return Response(accreditations, status=status.HTTP_200_OK)


#las lineas de codigo comentadas me estaban sirviendo para orientación 


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from international_accreditation.models import InternationalAccreditation
# from national_accreditation.models import NationalAccreditation
# from .serializers import AccreditationListSerializer

# class AccreditationListView(APIView):
#     def get(self, request):
#         international_accreditation = []
#         national_accreditation = []

#         for item in InternationalAccreditation.objects.all():
#             new_item = {}
#             new_item["id"] = item.id
#             new_item["created_at"] = item.created_at.date()
#             new_item["type"] = item.type
#             new_item["country"] = item.country.name

#             international_accreditation.append(new_item)

#             # print(InternationalAccreditation.objects.all())
#             # print(new_item)


#         for item in NationalAccreditation.objects.all():
#             new_item = {}
#             new_item["id"] = item.id
#             new_item["created_at"] = item.created_at.date()
#             new_item["type"] = item.type
#             new_item["country"] = "Panama"

#             national_accreditation.append(new_item)

#             #print(new_item)


#         accreditations = international_accreditation + national_accreditation
#         serializer = AccreditationListSerializer(data=accreditations, many=True)


#         if serializer.is_valid():
#             print(serializer.data)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




# from rest_framework.views import APIView
# from rest_framework.response import Response
# from international_accreditation.models import InternationalAccreditation
# from national_accreditation.models import NationalAccreditation
# from .serializers import AccreditationListSerializer

# class CombinedAccreditationView(APIView):
#     def get(self, request, *args, **kwargs):
        
#         international_data = InternationalAccreditation.objects.values(
#             'created_at', 'country__name', 'type', 'authorized_by', "id"
#         )
#         national_data = NationalAccreditation.objects.values(
#             'created_at', 'type', 'authorized_by', "id"
#         )


#         print(international_data)
#         combined_data = list(international_data)
#         if len(national_data)>0:
#             combined_data + list(national_data)

        
#         serializer = AccreditationListSerializer(combined_data, many=True)

#         return Response(serializer.data)





