from rest_framework import serializers

from housing.models import Housing, HousingPerson


class HousingPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingPerson
        fields = '__all__'


class HousingSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault())
    persons = HousingPersonSerializer(many=True, read_only=True)

    class Meta:
        model = Housing
        fields = '__all__'

    read_only_fields = [
        'created_at',
        'updated_at',
        'reviewed_comment',
        'reviewed_by',
        'authorized_comment',
        'authorized_by',
        'rejected_by',
        'status',
        'uuid',
        'certificated',
        'certification',
    ]
