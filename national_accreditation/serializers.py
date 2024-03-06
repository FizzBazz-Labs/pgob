from rest_framework import serializers

from national_accreditation.models import NationalAccreditation

from positions.serializers import PositionSerializer, SubPositionSerializer

from media_channels.serializers import MediaChannelSerializer

from security_accreditations.serializers import SecurityWeaponAccreditationSerializer


class NationalSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault())
    # security_weapon_accreditation = SecurityWeaponAccreditationSerializer(
    #     required=False)

    class Meta:
        model = NationalAccreditation
        fields = [
            'id',
            'image',
            'first_name',
            'last_name',
            'position',
            'sub_position',
            'media_channel',
            'authorization_letter',
            'institution',
            'security_weapon_accreditation',
            'address',
            'phone_number',
            'phone_number_2',
            'email',
            'birthday',
            'birthplace',
            'blood_type',
            'type',
            'status',
            # 'authorized_by'
            'created_by'
        ]


class NationalUpdateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = NationalAccreditation
        fields = [
            'id',
            'image',
            'first_name',
            'last_name',
            'position',
            'sub_position',
            'media_channel',
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
            'status',
            'created_by'
        ]
        # Make image and authorization_letter optional
        extra_kwargs = {
            'image': {'required': False},
            'authorization_letter': {'required': False},
        }


class NationalReadSerializer(NationalSerializer):
    position = PositionSerializer()
    sub_position = SubPositionSerializer()
    media_channel = MediaChannelSerializer()
