from rest_framework.permissions import BasePermission
from Music.models import User


class Super(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user.is_superuser or request.user.is_authenticated)

class UserPermission(BasePermission):
    def has_permission(self, request, view):
        # return bool(request.user.is_superuser)
        return bool( request.user.is_superuser or request.user.is_staff)