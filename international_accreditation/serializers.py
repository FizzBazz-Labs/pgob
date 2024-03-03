from rest_framework import serializers

from international_accreditation.models import InternationalAccreditation

from allergies.serializers import AllergySerializer

from immunizations.serializers import ImmunizationSerializer

from medical_histories.serializers import MedicalHistorySerializer

from media_channels.serializers import MediaChannelSerializer

from countries.serializers import CountrySerializer

from positions.serializers import PositionSerializer, SubPositionSerializer


class InternationalAccreditationSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = InternationalAccreditation
        fields = [
            'id',
            'country',
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
            'blood_group',
            'blood_rh_factor',
            'age',
            'diseases',
            'medication_1',
            'medication_2',
            'medication_3',
            'medication_4',
            'allergies',
            'immunizations',
            'medicals',
            'surgical',
            'doctor_name',
            'hotel_name',
            'hotel_address',
            'hotel_phone',
            'flight_arrival_date',
            'flight_arrival_time',
            'flight_arrival_number',
            'flight_from',
            'flight_departure_date',
            'flight_departure_time',
            'flight_departure_number',
            'flight_to',
            'type',
            # 'authorized_by',
            # 'authorized_by_position',
            'created_by',
        ]


class InternationalAccreditationReadSerializer(InternationalAccreditationSerializer):
    country = CountrySerializer()
    position = PositionSerializer()
    sub_position = SubPositionSerializer()
    media_channel = MediaChannelSerializer()
    allergies = AllergySerializer(many=True)
    immunizations = ImmunizationSerializer(many=True)
    medicals = MedicalHistorySerializer(many=True)
    flight_from = CountrySerializer()
    flight_to = CountrySerializer()
