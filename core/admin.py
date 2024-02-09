from django.contrib import admin
from .models import Country, Nationality, Position, MediaChannel, NationalAcreditation, InternationalAccreditation, SecurityAccreditation, FlightRequest, Vehicle, VehicleAccreditation, CommunicationEquipmentDeclaration, EquipmentItem, CommunicationEquipmentDeclarationEquipmentItem, GeneralVehicleAccreditation

modelos = [Country, Nationality, Position, MediaChannel, NationalAcreditation, InternationalAccreditation, SecurityAccreditation, FlightRequest, Vehicle, VehicleAccreditation, CommunicationEquipmentDeclaration, EquipmentItem, CommunicationEquipmentDeclarationEquipmentItem, GeneralVehicleAccreditation]

for modelo in modelos:
    admin.site.register(modelo)



# Register your models here.
