import binascii
import hashlib
import os
import random
import string

import pymongo
from core.settings import DATABASE
from dotenv import load_dotenv

from .errors import (
    AdminDoesNotExistError,
    AdminExistsError,
    InvalidAdminCredentialsError,
    InvalidAdminIDError,
)

load_dotenv()


class AdminAuth:
    def __init__(self) -> None:
        """
        Connect to MongoDB
        """
        client = pymongo.MongoClient(DATABASE["mongo_uri"])
        self.db = client[DATABASE["db"]][os.getenv("USER_DATA_COLLECTION")]

    def generate_admin_id(self) -> str:
        """Generates a unique admin id

        Args:
            None

        Returns:
            str
        """
        admin_id = "".join(
            random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits
            )
            for _ in range(16)
        )
        admin_id = "adm_" + admin_id

        if self.db.find_one({"user_id": admin_id}):
            admin_id = self.generate_admin_id()
        return admin_id

    def get_admin_id(self, email: str) -> str:
        """Fetches admin id for particular admin

        Args:
            email: Admin Email ID

        Returns:
            str
        """
        if value := self.db.find_one({"Email": email}):
            admin_id = value["user_id"]
            return admin_id

        raise AdminDoesNotExistError(f"Admin {email} Does Not Exist")

    def validate_admin_id(self, admin_id: str) -> bool:
        """Validates Admin id for particular admin

        Args:
            admin_id: Admin ID

        Returns:
            bool
        """
        value = self.db.find_one({"user_id": admin_id})
        if value and value["user_id"][0:3] == "adm":
            return True

        raise InvalidAdminIDError(f"Admin With admin_id {admin_id} NOT Found")

    def hash_password(self, pwd: str) -> str:
        """Hashes password using salted password hashing (SHA512 & PBKDF_HMAC2)

        Args:
            pwd: Password to be hashed

        Returns:
            str: Hashed password
        """
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")
        pwd_hash = hashlib.pbkdf2_hmac("sha512", pwd.encode("utf-8"), salt, 100000)
        pwd_hash = binascii.hexlify(pwd_hash)
        final_hashed_pwd = (salt + pwd_hash).decode("ascii")
        return final_hashed_pwd

    def check_hash(self, email: str, pwd: str) -> bool:
        """Verifies hashed password with stored hash & verifies Admin before login

        Args:
            email: Email ID of Admin
            pwd: Password to be checked

        Returns:
            bool
        """
        if value := self.db.find_one({"Email": email}):
            dbpwd = value["Password"]
            salt = dbpwd[:64]
            dbpwd = dbpwd[64:]

            pwd_hash = hashlib.pbkdf2_hmac(
                "sha512", pwd.encode("utf-8"), salt.encode("ascii"), 100000
            )
            pwd_hash = binascii.hexlify(pwd_hash).decode("ascii")

            if pwd_hash == dbpwd:
                return True
            else:
                raise InvalidAdminCredentialsError("Invalid Login Credentials")

        else:
            raise AdminDoesNotExistError("Admin Does Not Exist")

    def insert_admin(self, name: str, email: str, pwd: str) -> None:
        """Insert Admin into collection

        Args:
            name: Admin Name
            email: Admin Email ID
            pwd: Admin Account Password

        Returns:
            None: inserts Admin data into db
        """
        if self.db.find_one({"Email": email}):
            raise AdminExistsError("Admin Already Exists")
        else:
            pwd = self.hash_password(pwd)
            rec = {
                "user_id": self.generate_admin_id(),
                "Username": name,
                "Email": email,
                "Password": pwd,
            }
            self.db.insert_one(rec)
