from rest_framework import serializers
from core.models import NationalAccreditation


class NationalSerializer(serializers.ModelSerializer):
    class Meta:
        model = NationalAccreditation
        fields = [
            'image',
            'first_name',
            'last_name',
            'passport_id',
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
            # 'authorized_by'
            'created_by'
        ]
