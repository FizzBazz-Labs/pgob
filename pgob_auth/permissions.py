from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Admin').exists()


class IsReviewer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Reviewer').exists()


class IsAccreditor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Accreditor').exists()


class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='User').exists()


class HasNational(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.accreditations.filter(name='National').exists()


class HasInternational(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.accreditations.filter(name='International').exists()


class HasVehicleAccessAirport(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.accreditations.filter(name='VehicleAccessAirport').exists()


class HasGeneralVehicle(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.accreditations.filter(name='GeneralVehicle').exists()


class HasAircraft(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.accreditations.filter(name='Aircraft').exists()


class HasCommunicationEquipment(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.accreditations.filter(name='CommunicationEquipment').exists()


class HasSecurity(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.accreditations.filter(name='Security').exists()
