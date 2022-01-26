import unittest

from authentication.jwt import TokenAuth


class Test_JWT(unittest.TestCase):
    def __init__(self):
        self.Token_Auth = TokenAuth()

    def test_jwt_generation(self):
        token = self.Token_Auth.generate_token(
            payload={"ID": "ABC"}, expiry=1, get_refresh=False
        )
        data = self.Token_Auth.verify_token(token=token)
        print("Data:", data)
        self.assertEqual("ABC", data["ID"])
        self.assertEqual("user", data["role"])

    def test_refresh_generation(self):
        token = self.Token_Auth.generate_token(
            payload={"ID": "ABC"}, expiry=1, get_refresh=True
        )
        self.assertIn("access_token", token)
        self.assertIn("refresh_token", token)

    def test_decode_token(self):
        token = self.oken_Auth.generate_token(
            payload={"ID": "ABC"}, expiry=1, get_refresh=True
        )
        bool_val, data = self.Token_Auth.decode_token(token=token)
        print("Data:", data)
        self.assertTrue(bool_val)
        self.assertEqual("ABC", data["ID"])
        self.assertEqual("user", data["role"])
