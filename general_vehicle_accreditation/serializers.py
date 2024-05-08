from django.contrib.auth import get_user_model

from rest_framework import serializers

from general_vehicle_accreditation.models import GeneralVehicleAccreditation

from vehicles.serializers import VehicleSerializer

from countries.models import Country

from core.serializers import UserSerializer


class GeneralVehicleAccreditationSerializer(serializers.ModelSerializer):
    # accreditation_type = serializers.CharField()
    created_by = serializers.PrimaryKeyRelatedField(
        required=False, read_only=True)

    country = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(), default=Country.objects.get(name='Panamá').pk)

    fullname = serializers.SerializerMethodField()

    class Meta:
        model = GeneralVehicleAccreditation
        fields = [
            'accreditation_type',
            'id',
            'country',
            'assigned_to',
            'vehicles',
            'fullname',
            'distinctive',
            'observations',
            'created_by',
            'status',
        ]

    def to_internal_value(self, data):
        internal_values = super().to_internal_value(data)

        if 'created_by' not in data and 'request' in self.context:
            internal_values['created_by'] = self.context['request'].user

        return internal_values

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_by'] = UserSerializer(instance.created_by).data

        return representation

    def get_fullname(self, obj):
        return f'{obj.created_by.first_name} {obj.created_by.last_name}'


class GeneralVehicleAccreditationReadSerializer(GeneralVehicleAccreditationSerializer):
    vehicles = VehicleSerializer(many=True, read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_by'] = UserSerializer(instance.created_by).data

        return representation
