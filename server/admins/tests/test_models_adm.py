from dotenv import load_dotenv
import unittest

from admins.models import AdminAuth
from admins.errors import (
    InvalidAdminCredentialsError,
    AdminDoesNotExistError,
    InvalidAdminIDError,
)


class Test_Admin_Model(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:

        load_dotenv()

        cls.adminauth = AdminAuth()

    def setUp(self) -> None:
        self.adminauth.insert_admin("adminuser", "testmail@gmail.com", "testpwd")

    def test_aid_functions(self) -> None:
        aid = self.adminauth.get_admin_id("testmail@gmail.com")

        with self.assertRaises(InvalidAdminIDError):
            self.adminauth.validate_admin_id("wrongaid")

        with self.assertRaises(AdminDoesNotExistError):
            self.adminauth.get_admin_id("wrongemail@gmail.com")

        self.assertTrue(self.adminauth.validate_admin_id(aid))

    def test_hash(self):
        pwd = "testpwd"

        with self.assertRaises(AdminDoesNotExistError):
            self.adminauth.check_hash("wrongemail@gmail.com", pwd)

        with self.assertRaises(InvalidAdminCredentialsError):
            self.adminauth.check_hash("testmail@gmail.com", "wrongpwd")

        self.assertTrue(self.adminauth.check_hash("testmail@gmail.com", pwd))

    def tearDown(self) -> None:
        self.adminauth.db.remove({"Email": "testmail@gmail.com"})
