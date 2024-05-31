from rest_framework import serializers

from allergies.models import Allergy
from allergies.serializers import AllergySerializer
from countries.serializers import CountrySerializer
from immunizations.models import Immunization
from immunizations.serializers import ImmunizationSerializer
from media_channels.serializers import MediaChannelSerializer
from medical_histories.models import MedicalHistory
from medical_histories.serializers import MedicalHistorySerializer
from positions.serializers import PositionSerializer, SubPositionSerializer

from core.serializers import UserSerializer

from countries.serializers import CountrySerializer

from international_accreditation.models import InternationalAccreditation
from international_accreditation.models import InternationalAccreditation as International


class InternationalAccreditationSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    allergies = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Allergy.objects.all())
    immunizations = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Immunization.objects.all())
    medicals = serializers.PrimaryKeyRelatedField(
        many=True, queryset=MedicalHistory.objects.all())

    class Meta:
        model = InternationalAccreditation
        fields = [
            'id',
            'country',
            'image',
            'first_name',
            'last_name',
            'passport_id',
            'passport_id_image',
            'private_insurance',
            'position',
            'sub_position',
            'media_channel',
            'authorization_letter',
            'institution',
            'authorized_comment',
            'address',
            'phone_number',
            'phone_number_2',
            'email',
            'birthday',
            'birthplace',
            'security_weapon_accreditation',

            # Medical Information
            'blood_type',
            'diseases',
            'medication_1',
            'medication_2',
            'medication_3',
            'medication_4',
            'allergies',
            'allergies_description',
            'immunizations',
            'medicals',
            'surgical',
            'doctor_name',

            'hotel_name',
            'hotel_address',
            'hotel_phone',
            'flight_arrival_datetime',
            'flight_arrival_number',
            'flight_arrival_airport',
            'flight_from',
            'flight_departure_datetime',
            'flight_departure_number',
            'flight_departure_airport',
            'flight_to',
            'type',
            'status',
            'created_by',
            'times_edited',
            'certificated',
            'uuid',
            'security_weapon_accreditation',
            'allergies_description',
            'reviewed_comment',

            'certification',
        ]

        extra_kwargs = {
            'certificated': {'read_only': True},
            'uuid': {'read_only': True},
            'certification': {'read_only': True},
        }

    def create(self, validated_data):
        passport_id = validated_data.get('passport_id')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')

        already_exists = International.objects.filter(
            passport_id=passport_id,
            first_name=first_name,
            last_name=last_name
        ).exists()

        if already_exists:
            raise serializers.ValidationError({
                'error': 'There is already an accreditation with this passport id, first name or last name.'
            })

        allergies_data = validated_data.pop('allergies', [])
        immunizations_data = validated_data.pop('immunizations', [])
        medicals_data = validated_data.pop('medicals', [])

        user = self.context['request'].user
        validated_data['country'] = user.profile.country

        instance = super().create(validated_data)

        instance.allergies.set(allergies_data)
        instance.immunizations.set(immunizations_data)
        instance.medicals.set(medicals_data)

        return instance

    def to_internal_value(self, data):

        country = data.get('country')

        if country == '0':
            data['country'] = self.context['request'].user.profile.country.id

        return super().to_internal_value(data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['flight_from'] = CountrySerializer(
            instance.flight_from).data
        representation['flight_to'] = CountrySerializer(
            instance.flight_to).data
        representation
        representation['created_by'] = UserSerializer(instance.created_by).data
        representation['position'] = PositionSerializer(
            instance.position).data
        if instance.sub_position:
            representation['sub_position'] = SubPositionSerializer(
                instance.sub_position).data
        return representation


class InternationalAccreditationUpdateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = InternationalAccreditation
        fields = [
            'id',
            # 'country',
            'image',
            'first_name',
            'last_name',
            'passport_id',
            'private_insurance',
            'position',
            'sub_position',
            'media_channel',
            'authorized_comment',
            'authorization_letter',
            'institution',
            'address',
            'phone_number',
            'phone_number_2',
            'email',
            'birthday',
            'birthplace',
            'blood_type',
            'diseases',
            'medication_1',
            'medication_2',
            'medication_3',
            'medication_4',
            'allergies',
            'allergies_description',
            'immunizations',
            'medicals',
            'surgical',
            'doctor_name',
            'hotel_name',
            'hotel_address',
            'hotel_phone',
            'flight_arrival_datetime',
            'flight_arrival_number',
            'flight_from',
            'flight_departure_datetime',
            'flight_departure_number',
            'times_edited',
            'flight_to',
            'type',
            'created_by',
            'status',
            'allergies_description',
        ]
        extra_kwargs = {
            'image': {'required': False},
            'authorization_letter': {'required': False},
            # Add extra kwargs for many-to-many fields to make them read-only
        }

    def update(self, instance, validated_data):
        # Update many-to-many fields
        self.update_many_to_many(instance, 'allergies', validated_data)
        self.update_many_to_many(instance, 'immunizations', validated_data)
        self.update_many_to_many(instance, 'medicals', validated_data)

        # Update other fields
        for field, value in validated_data.items():
            setattr(instance, field, value)

        instance.save()
        return instance

    def update_many_to_many(self, instance, field_name, validated_data):
        field_data = validated_data.pop(field_name, None)
        if field_data is not None:
            # Set the many-to-many relationships
            getattr(instance, field_name).set(field_data)
        elif field_name in validated_data:
            # If the field is provided but empty, clea
            getattr(instance, field_name).clear()


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
