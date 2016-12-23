from rest_framework import permissions
from rest_framework.compat import is_authenticated


class IsAdminProjectOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS or
            request.user and
            is_authenticated(request.user) and
            request.user.is_admin
        )
