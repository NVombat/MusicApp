from datetime import datetime, timedelta
from dotenv import load_dotenv
import jwt
import os

from .errors import InvalidTokenError, TokenGenerationError

load_dotenv()


class TokenAuth:
    def __init__(self):
        """
        Key for JWT
        """
        self.signature = os.getenv("SECRET_KEY")

    def generate_token(
        self, payload: dict, expiry: int = 1, get_refresh: bool = False, **kwargs
    ):
        """Generates a unique JWT Token

        Args:
            payload: Data To Be Encoded
            expiry: Valid Hours
            get_refresh
            kwargs

        Returns:
            dict/str -> token
        """
        try:
            current_time = datetime.utcnow()
            payload["exp"] = current_time + timedelta(hours=expiry)
            payload["role"] = "user"
            access_token = jwt.encode(payload, key=self.signature, algorithm="HS256")

            if get_refresh:
                if value := kwargs.get("refresh_exipry"):
                    payload["exp"] = current_time + timedelta(hours=value)
                refresh_payload = {**{"refresh": True}, **payload}
                refresh_token = jwt.encode(
                    refresh_payload, key=self.signature, algorithm="HS256"
                )
                return {"access_token": access_token, "refresh_token": refresh_token}

            return access_token
        except Exception:
            raise TokenGenerationError("Error While Generating JWT Tokens")

    def decode_token(self, token: str) -> tuple:
        """Decodes Token To Give Encoded Data

        Args:
            token: Encoded Token

        Returns:
            tuple(bool, dict)
        """
        try:
            data = jwt.decode(
                token,
                key=self.signature,
                options={"verify_exp": True, "verify_signature": True},
                algorithms=["HS256"],
            )

            if data:
                return (True, data)
            return (False, None)

        except jwt.exceptions.InvalidTokenError:
            raise InvalidTokenError("JWT Token Is Invalid")
        except jwt.exceptions.ExpiredSignatureError:
            raise InvalidTokenError("JWT Token Is Invalid")
        except jwt.exceptions.DecodeError:
            raise InvalidTokenError("JWT Token Decode Failed")

    def decode_refresh_token(self, token: str) -> dict:
        """Decodes Refresh Token To Give Encoded Data

        Args:
            token: Encoded Refresh Token

        Returns:
            dict
        """
        try:
            data = jwt.decode(
                token,
                key=self.signature,
                options={"verify_exp": False, "verify_signature": True},
                algorithms=["HS256"],
            )

            if data["refresh"] == True and data["role"] == "user":
                return data

            return None

        except Exception:
            raise InvalidTokenError(
                "Error Decoding Refresh Token - Token or Role Invalid"
            )

    def verify_token(self, token: str):
        try:
            token = jwt.decode(
                jwt=token.encode(),
                key=self.signature,
                options={"verify_exp": True, "verify_signature": True},
                algorithms=["HS256"],
            )
            return token
        except Exception:
            return None
