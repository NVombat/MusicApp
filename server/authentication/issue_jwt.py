from dotenv import load_dotenv
import jwt
import os

load_dotenv()

class TokenAuth:
    def __init__(self):
        self.signature = os.getenv("SECRET_KEY")

    def generate_key(self,):
        pass