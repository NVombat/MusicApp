from datetime import datetime, timedelta
from dotenv import load_dotenv
import jwt
import os

load_dotenv()


class TokenAuth:
    def __init__(self):
        self.signature = os.getenv("SECRET_KEY")

    def generate_token(self, payload: dict, expiry: int=1, get_refresh: bool=False, **kwargs):
        current_time = datetime.utcnow()
        payload["exp"] = current_time + timedelta(hours=expiry)
        access_token = jwt.encode(payload, key=self.signature)

        if get_refresh:
            if value := kwargs.get("refresh_exipry"):
                payload["exp"] = current_time + timedelta(seconds=value)
            refresh_payload = {**{"refresh": True}, **payload}
            refresh_token = jwt.encode(refresh_payload, key=self.signature)
            return {"access_token": access_token, "refresh_token": refresh_token}

        return access_token

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
