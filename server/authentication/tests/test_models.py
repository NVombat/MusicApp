from dotenv import load_dotenv
import unittest

from authentication.models import UserAuth, ContactUsData
from authentication.errors import (
    ContactUsDataInsertionError,
    InvalidUserCredentialsError,
    UserDoesNotExistError,
    InvalidUIDError,
)


class Test_Auth_Model(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:

        load_dotenv()

        cls.userauth = UserAuth()
        cls.contactus = ContactUsData()

    def setUp(self) -> None:
        self.userauth.insert_user("testmail@gmail.com", "testpwd")

    def test_uid_functions(self) -> None:
        uid = self.userauth.get_uid("testmail@gmail.com")

        with self.assertRaises(InvalidUIDError):
            self.userauth.validate_uid("wronguid")

        with self.assertRaises(UserDoesNotExistError):
            self.userauth.get_uid("wrongemail@gmail.com")

        self.assertTrue(self.userauth.validate_uid(uid))

    def test_hash(self):
        pwd = "testpwd"

        with self.assertRaises(UserDoesNotExistError):
            self.userauth.check_hash("wrongemail@gmail.com", pwd)

        with self.assertRaises(InvalidUserCredentialsError):
            self.userauth.check_hash("testmail@gmail.com", "wrongpwd")

        self.assertTrue(self.userauth.check_hash("testmail@gmail.com", pwd))

    def test_contact_us(self):
        message = "testmessage"

        with self.assertRaises(ContactUsDataInsertionError):
            self.userauth.insert_contact_us_data("Test User", message)

        self.assertTrue(
            self.userauth.insert_contact_us_data(
                "Test User", "testmail.gmail.com", message
            )
        )

    def tearDown(self) -> None:
        self.userauth.db.remove({"Email": "testmail@gmail.com"})
        self.contactus.db.remove({"Email": "testmail@gmail.com"})
