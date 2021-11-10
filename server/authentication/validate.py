from rest_framework.permissions import BasePermission

from .errors import InvalidUIDError
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
            User_Auth.validate_uid(token)

        except InvalidUIDError as iue:
            print("Error:", str(iue))
            return False

        setattr(request, "user_id", token)
        print(request.user_id)
        return True