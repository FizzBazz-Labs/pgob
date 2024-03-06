from rest_framework import permissions


class Is(permissions.BasePermission):
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
