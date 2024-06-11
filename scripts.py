import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pgob.settings')
django.setup()

if __name__ == '__main__':
    from commerce.models import Commerce, CommerceEmployee
    from housing.models import Housing, HousingPerson
    from security_accreditations.models import SecurityWeaponAccreditation as Security
    from national_accreditation.models import NationalAccreditation as National
    from intercom_equipment_declaration.models import IntercomEquipmentDeclaration as Equipment
    from overflight_non_commercial_aircraft.models import OverflightNonCommercialAircraft as Aircraft
    from general_vehicle_accreditation.models import GeneralVehicleAccreditation as GeneralVehicle
    from international_accreditation.models import InternationalAccreditation as International
    from vehicles.models import Vehicle

    print('Updating commerce records')
    for item in Commerce.objects.all():
        item.admin_name = item.admin_name.title()
        item.save()

    print('Updating commerce employee records')
    for item in CommerceEmployee.objects.all():
        item.first_name = item.first_name.title()
        item.last_name = item.last_name.title()
        item.save()

    print('Updating housing records')
    for item in Housing.objects.all():
        if item.building_admin_name is not None:
            item.building_admin_name = item.building_admin_name.title()

        if item.owner_name is not None:
            item.owner_name = item.owner_name.title()

        item.save()

    print('Updating housing person records')
    for item in HousingPerson.objects.all():
        item.first_name = item.first_name.title()
        item.last_name = item.last_name.title()
        item.save()

    print('Updating security records')
    for item in Security.objects.all():
        if item.name is not None:
            item.name = item.name.title()
        item.save()

    print('Updating equipment records')
    for item in Equipment.objects.all():
        item.institution = item.institution.title()
        item.save()

    print('Updating aircraft records')
    for item in Aircraft.objects.all():
        item.pmi_name = item.pmi_name.title()
        item.save()

    print('Updating general vehicle records')
    for item in GeneralVehicle.objects.all():
        item.assigned_to = item.assigned_to.title()
        item.save()

    print('Updating vehicle records')
    for item in Vehicle.objects.all():
        item.driver_name = item.driver_name.title()
        item.save()

    print('Updating national records')
    for item in National.objects.all():
        item.first_name = item.first_name.title()
        item.last_name = item.last_name.title()
        item.save()

    print('Updating international records')
    for item in International.objects.all():
        item.first_name = item.first_name.title()
        item.last_name = item.last_name.title()
        item.save()
