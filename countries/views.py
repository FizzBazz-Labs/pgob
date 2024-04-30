from rest_framework.generics import ListAPIView

from countries.models import Country

from countries.serializers import CountrySerializer


class CountriesListApiView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = None
