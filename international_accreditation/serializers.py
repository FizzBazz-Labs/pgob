from rest_framework import serializers

from allergies.models import Allergy
from allergies.serializers import AllergySerializer
from countries.serializers import CountrySerializer
from immunizations.models import Immunization
from immunizations.serializers import ImmunizationSerializer
from international_accreditation.models import InternationalAccreditation
from media_channels.serializers import MediaChannelSerializer
from medical_histories.models import MedicalHistory
from medical_histories.serializers import MedicalHistorySerializer
from positions.serializers import PositionSerializer, SubPositionSerializer


class InternationalAccreditationSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

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
            'private_insurance',
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
            'security_weapon_accreditation',
            'blood_type',
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
            'flight_arrival_datetime',
            'flight_arrival_number',
            'flight_from',
            'flight_departure_datetime',
            'flight_departure_number',
            'flight_to',
            'type',
            'status',
            'created_by',
            'downloaded',
            'uuid',
            'security_weapon_accreditation',
            'allergies_description',
        ]

        extra_kwargs = {
            'downloaded': {'read_only': True},
            'uuid': {'read_only': True},
        }

    def create(self, validated_data):
        print("Before popping 'allergies':", validated_data)
        allergies_data = validated_data.pop('allergies', [])
        print("After popping 'allergies':", validated_data)
        print("Extracted allergies data:", allergies_data)
        # allergies_data = validated_data.pop('allergies', [])
        immunizations_data = validated_data.pop('immunizations', [])
        medicals_data = validated_data.pop('medicals', [])

        instance = super().create(validated_data)

        instance.allergies.set(allergies_data)
        instance.immunizations.set(immunizations_data)
        instance.medicals.set(medicals_data)

        return instance


class InternationalAccreditationUpdateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = InternationalAccreditation
        fields = [
            'id',
            'country',
            'image',
            'first_name',
            'last_name',
            'passport_id',
            'private_insurance',
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
