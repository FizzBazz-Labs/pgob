from rest_framework.routers import DefaultRouter

from housing.views import HousingViewSet, HousingPersonViewSet
from commerce.views import CommerceViewSet, CommerceEmployeeViewSet
from general_vehicle_accreditation.views import GeneralVehicleViewSet
from overflight_non_commercial_aircraft.views import OverflightNonCommercialAircraftViewSet
from vehicle_access_airport_accreditations.views import AirportVehicleAccessViewSet
from intercom_equipment_declaration.views import IntercomEquipmentDeclarationViewSet
from security_accreditations.views import SecurityWeaponViewSet
from national_accreditation.views import NationalViewSet
from international_accreditation.views import InternationalViewSet
from vehicles.views import VehicleViewSet

router = DefaultRouter()

router.register(r'housings', HousingViewSet)
router.register(r'housing-persons', HousingPersonViewSet)
router.register(r'commerces', CommerceViewSet)
router.register(r'commerce-employees', CommerceEmployeeViewSet)
router.register(r'general-vehicles', GeneralVehicleViewSet)
router.register(r'aircrafts', OverflightNonCommercialAircraftViewSet)
router.register(r'airport-vehicle-access', AirportVehicleAccessViewSet)
router.register(r'intercommunication-equipments', IntercomEquipmentDeclarationViewSet)
router.register(r'security-weapons', SecurityWeaponViewSet)
router.register(r'nationals', NationalViewSet)
router.register(r'internationals', InternationalViewSet)
router.register(r'vehicles', VehicleViewSet)
