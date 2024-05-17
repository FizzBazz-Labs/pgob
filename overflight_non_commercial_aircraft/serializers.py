from rest_framework import serializers

from overflight_non_commercial_aircraft.models import OverflightNonCommercialAircraft

from countries.serializers import CountrySerializer

from positions.serializers import PositionSerializer, SubPositionSerializer

from core.serializers import UserSerializer


class OverflightNonCommercialAircraftSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = OverflightNonCommercialAircraft
        fields = [
            'id',
            'country',
            'aircraft_type',
            'model',
            'flight_type',
            'fbo_attendant',
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
            'category',
            # 'signature',
            'created_by',
            'status',
        ]

    def to_internal_value(self, data):
        data['country'] = self.context['request'].user.profile.country.pk
        return super().to_internal_value(data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['created_by'] = UserSerializer(instance.created_by).data

        try:
            representation['flight_type'] = instance.get_flight_type_display()
            representation['category'] = instance.get_category_display()
            representation['aircraft_type'] = instance.get_aircraft_type_display()
        except:
            pass

        return representation


class OverflightNonCommercialAircraftReadSerializer(OverflightNonCommercialAircraftSerializer):
    country = CountrySerializer()
    position = PositionSerializer()
    sub_position = SubPositionSerializer()
    created_by = UserSerializer()
