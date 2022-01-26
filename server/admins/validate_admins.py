from rest_framework.permissions import BasePermission

from authentication.errors import InvalidTokenError
from . import Admin_Token_Auth, Admin_Auth
from .errors import InvalidAdminIDError


class ValidateAdmin(BasePermission):
    def has_permission(self, request, view):
        try:
            hdrs = request.headers
            token_type, token = hdrs["Authorization"].split()
            assert token_type == "Bearer"

        except Exception:
            print("Error In Getting Tokens From Header")
            return False

        try:
            bool_val, data = Admin_Token_Auth.decode_token(token)
            print(bool_val, data)
            assert bool_val == True

        except InvalidTokenError as ite:
            print("Error:", str(ite))
            return False
        except Exception:
            print("Error In Decoding Token")
            return False

        try:
            admin_id = data["aid"]
            Admin_Auth.validate_admin_id(admin_id)
            assert data["role"] == "admin"

        except InvalidAdminIDError as iaie:
            print("Error:", str(iaie))
            return False
        except Exception:
            print("Error In Authenticating Admin")
            return False

        setattr(request, "admin_id", admin_id)
        # request.session["admin_id"] = admin_id
        return True
