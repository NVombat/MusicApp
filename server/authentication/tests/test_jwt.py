import unittest

from authentication import Token_Auth


class Test_JWT(unittest.TestCase):

    def test_jwt_generation(self):
        token = Token_Auth.generate_token(
            payload={"ID": "ABC"}, expiry=1, get_refresh=False
        )
        data = self.auth_token.verify_key(key=token)
        self.assertIn("ID", data)

    def test_refresh_generation(self):
        token = Token_Auth.generate_token(
            payload={"ID": "ABC"}, expiry=1, get_refresh=True
        )
        self.assertIn("access_token", token)
        self.assertIn("refresh_token", token)

    def test_decoding(self):
        pass
