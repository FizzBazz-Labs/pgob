from django_filters import FilterSet
from .models import Housing, HousingPerson


class HousingFilterSet(FilterSet):
    class Meta:
        model = Housing
        fields = {
            'status': ['exact'],
            'persons__first_name': ['exact', 'icontains'],
        }
