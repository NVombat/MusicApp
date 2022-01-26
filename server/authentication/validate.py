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
            bool_val, data = Token_Auth.decode_token(token)
            print(bool_val, data)
            assert bool_val == True

        except InvalidTokenError as ite:
            print("Error:", str(ite))
            return False
        except Exception:
            print("Error In Decoding Token")
            return False

        try:
            user_id = data["id"]
            User_Auth.validate_uid(user_id)
            assert data["role"] == "user"

        except InvalidUIDError as iue:
            print("Error:", str(iue))
            return False
        except Exception:
            print("Error In Authenticating User")
            return False

        setattr(request, "user_id", user_id)
        # request.session["user_id"] = user_id
        return True
