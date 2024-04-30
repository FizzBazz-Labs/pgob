from rest_framework import serializers

from commerce.models import Commerce


class CommerceSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Commerce
        fields = '__all__'

        read_only_fields = [
            'created_at',
            'updated_at',
            'downloaded',
            'reviewed_comment',
            'reviewed_by',
            'authorized_comment',
            'authorized_by',
            'rejected_by',
            'status',
            'uuid',
            'qr_code',
        ]
