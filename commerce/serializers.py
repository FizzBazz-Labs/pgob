from rest_framework import serializers

from commerce.models import Commerce, CommerceEmployee


class CommerceEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommerceEmployee
        fields = '__all__'


class CommerceSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    employees = CommerceEmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Commerce
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
