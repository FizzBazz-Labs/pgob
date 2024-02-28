from rest_framework import serializers

from overflight_non_commercial_aircraft.models import OverflightNonCommercialAircraft


class OverflightNonCommercialAircraftSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    country_id = serializers.IntegerField(write_only=True)
    country = serializers.StringRelatedField()
    position_id = serializers.IntegerField(write_only=True)
    position = serializers.StringRelatedField()
    sub_position_id = serializers.IntegerField(write_only=True)
    sub_position = serializers.StringRelatedField()

    class Meta:
        model = OverflightNonCommercialAircraft
        fields = [
            'country',
            'country_id',
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
            'position_id',
            'sub_position',
            'sub_position_id',
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
            'signature',
            'created_by',

        ]
