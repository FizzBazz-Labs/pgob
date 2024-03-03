from rest_framework import serializers

from overflight_non_commercial_aircraft.models import OverflightNonCommercialAircraft

from countries.serializers import CountrySerializer

from positions.serializers import PositionSerializer, SubPositionSerializer

class OverflightNonCommercialAircraftSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = OverflightNonCommercialAircraft
        fields = [
            'country',
            'aircraft_type',
            'model',
            'jurisdiction',
            'registration',
            'color',
            'call_sign',
            'commander_name',
            'crew_members_count',
            'pmi_name',
            'position',
            'sub_position',
            'passengers_count',
            'arrival_date',
            'departure_date',
            'overflight_info',
            'landing_info',
            'origin',
            'destination',
            'route',
            'ground_facilities',
            'date',
            #'signature',
            'created_by',

        ]

class OverflightNonCommercialAircraftReadSerializer(OverflightNonCommercialAircraftSerializer):
    country = CountrySerializer()
    position = PositionSerializer()
    sub_position = SubPositionSerializer()