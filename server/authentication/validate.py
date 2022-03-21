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
            return False

        try:
            bool_val, data = Token_Auth.decode_token(token)
            assert bool_val == True

        except InvalidTokenError:
            return False
        except Exception:
            return False

        try:
            user_id = data["id"]
            User_Auth.validate_uid(user_id)
            assert data["role"] == "user"

        except InvalidUIDError:
            return False
        except Exception:
            return False

        setattr(request, "user_id", user_id)
        # request.session["user_id"] = user_id
        return True
