from rest_framework import serializers

from national_accreditation.models import NationalAccreditation

from positions.serializers import PositionSerializer, SubPositionSerializer


class NationalSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    position_id = serializers.IntegerField(write_only=True)
    position = serializers.StringRelatedField()
    sub_position_id = serializers.IntegerField(write_only=True)
    sub_position = serializers.StringRelatedField()
    media_channel_id = serializers.IntegerField(write_only=True)
    media_channel = serializers.StringRelatedField()

    class Meta:
        model = NationalAccreditation
        fields = [
            'image',
            'first_name',
            'last_name',
            'passport_id',
            'position',
            'position_id',
            'sub_position',
            'sub_position_id',
            'media_channel',
            'media_channel_id',
            'authorization_letter',
            'institution',
            'address',
            'phone_number',
            'phone_number_2',
            'email',
            'birthday',
            'birthplace',
            'blood_type',
            'type',
            # 'authorized_by'
            'created_by'
        ]
