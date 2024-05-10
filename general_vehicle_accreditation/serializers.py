from rest_framework import serializers

from general_vehicle_accreditation.models import GeneralVehicleAccreditation as GeneralVehicle


class GeneralVehicleSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = GeneralVehicle
        fields = '__all__'
        read_only_fields = [
            'created_at',
            'updated_at',
            'reviewed_by',
            'authorized_by',
            'rejected_by',
            'status',
            'uuid',
            'certificated',
            'certificated',
        ]
