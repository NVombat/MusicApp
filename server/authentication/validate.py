from rest_framework.permissions import BasePermission

from .errors import InvalidTokenError
from . import User_Auth


class ValidateUser(BasePermission):
    def has_permission(self, request, view):
        try:
            hdrs = request.headers
            token_type, token = hdrs["Authorization"].split()
            assert token_type == "Bearer"

        except Exception:
            print("Error In Getting Tokens From Header")
            return False

        try:
            User_Auth.validate_uid()

        except InvalidTokenError as ite:
            print("Error:", str(ite))
            return False

        setattr(request, "user_id", token)
        return True
