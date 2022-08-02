
from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_staff and request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_staff and request.user.is_superuser


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
