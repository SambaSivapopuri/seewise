from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

class IsValidToken(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            JWTAuthentication().authenticate(request)
            return True
        except AuthenticationFailed:
            return False
        