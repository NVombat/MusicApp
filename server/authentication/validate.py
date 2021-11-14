from rest_framework.permissions import BasePermission

from .errors import InvalidTokenError, InvalidUIDError
from . import User_Auth, Token_Auth


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
            data = Token_Auth.decode_token(token)

        except InvalidTokenError as ite:
            print("Error:", str(ite))
            return False

        try:
            user_id = data[1]["id"]
            User_Auth.validate_uid(user_id)

        except InvalidUIDError as iue:
            print("Error:", str(iue))
            return False

        setattr(request, "user_id", token)
        return True
