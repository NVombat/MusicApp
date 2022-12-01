import binascii
import hashlib
import os
import random
import string
from datetime import datetime

import pymongo
from core.settings import DATABASE
from dotenv import load_dotenv

from .errors import (ContactUsDataInsertionError, InvalidQIDError,
                     InvalidUIDError, InvalidUserCredentialsError,
                     InvalidVerificationError, NoContactUsQueriesFoundError,
                     UserDoesNotExistError, UserExistsError)

load_dotenv()


class UserAuth:
    def __init__(self) -> None:
        """
        Connect to MongoDB
        """
        client = pymongo.MongoClient(DATABASE["mongo_uri"])
        self.db = client[DATABASE["db"]][os.getenv("USER_DATA_COLLECTION")]

    def generate_uid(self) -> str:
        """Generates a unique user id

        Args:
            None

        Returns:
            str
        """
        uid = "".join(
            random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits
            )
            for _ in range(16)
        )

        if self.db.find_one({"user_id": uid}):
            uid = self.generate_uid()
        return uid

    def get_uid(self, email: str) -> str:
        """Fetches user id for particular user

        Args:
            email: User Email ID

        Returns:
            str
        """
        if value := self.db.find_one({"Email": email}):
            uid = value["user_id"]
            return uid

        raise UserDoesNotExistError(f"User {email} Does Not Exist")

    def validate_uid(self, uid: str) -> bool:
        """Validates user id for particular user

        Args:
            uid: User ID

        Returns:
            bool
        """
        value = self.db.find_one({"user_id": uid})
        if value:
            return True

        raise InvalidUIDError(f"User With user_id {uid} NOT Found")

    def insert_user(self, email: str, pwd: str) -> None:
        """Insert user into collection

        Args:
            name: User Name
            email: User Email ID
            pwd: User Account Password

        Returns:
            None: inserts user data into db
        """
        if self.db.find_one({"Email": email}):
            raise UserExistsError("User Already Exists")
        else:
            pwd = self.hash_password(pwd)
            rec = {
                "user_id": self.generate_uid(),
                "Email": email,
                "Password": pwd,
                "ContactUs": [], # Query ID
                "Likes": [], # Like ID
                "Comments": [], # Comment ID
                "Notes": [] # Notes on When Password was Last Changed - FOR ADMIN
            }
            self.db.insert_one(rec)

    def get_contact_us_query_ids(self, email: str) -> list:
        """Fetches contact us query ids for particular user

        Args:
            email: User Email ID

        Returns:
            list
        """
        if value := self.db.find_one({"Email": email}):
            query_ids = value["ContactUs"]
            if isinstance(query_ids, list) and len(query_ids)>0:
                return query_ids
            else:
                raise NoContactUsQueriesFoundError(f"User {email} Has No Contact Us Queries Raised")

        raise UserDoesNotExistError(f"User {email} Does Not Exist")

    def add_verif_code(self, email: str, check_recursive_correctness: int) -> int:
        """Adds verification code & timestamp for reset password functionality

        Args:
            email: User Email ID
            check_recursive_correctness: Value to check recursive function

        Returns:
            int: Verification code generated for the user
        """
        # To check if recursive call is working correctly
        # if check_recursive_correctness==0:
        #     verif_code = 883330
        # else:
        #    verif_code = random.randint(100000, 999999)
        verif_code = random.randint(100000, 999999)

        if self.db.find_one({"verif_code": verif_code}):
            verif_code = self.add_verif_code(email, 1)

        else:
            verif_code_init_timestamp = datetime.now()
            self.db.update_one(
                {"Email": email},
                {
                    "$set": {
                        "verif_code": verif_code,
                        "timestamp_created": verif_code_init_timestamp,
                    }
                },
            )

            return verif_code

    def check_verif_code(self, code: int) -> bool:
        """Checks if verification code is valid

        Args:
            code: Verification Code

        Returns:
            bool
        """
        # Time when user enters the verification code
        verif_code_entry_time = datetime.now()

        if value := self.db.find_one({"verif_code": code}):
            email = value["Email"]
            # Time when verification code was generated
            timetamp_created = value["timestamp_created"]

            if (verif_code_entry_time - timetamp_created).total_seconds() > 3600:
                self.db.update_one(
                    {"Email": email},
                    {"$unset": {"verif_code": "", "timestamp_created": ""}},
                )
                raise InvalidVerificationError("Verification Code Expired!")
            else:
                return True

        raise InvalidVerificationError("Invalid Verification Code")

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
        """Verifies hashed password with stored hash & verifies user before login

        Args:
            email: Email ID of User
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
                raise InvalidUserCredentialsError("Invalid Login Credentials")

        else:
            raise UserDoesNotExistError("User Does Not Exist")

    def reset_password(self, pwd: str, code: int) -> bool:
        """Resets user password to updated password and deletes verification code

        Args:
            pwd: New Password
            code: Verification code

        Returns:
            bool
        """
        if value := self.db.find_one({"verif_code": code}):
            email = value["Email"]

            pwd_change_time = datetime.now()
            pct_string = pwd_change_time.strftime("%d/%m/%Y %H:%M:%S")
            msg = "Password Changed: " + pct_string

            self.db.find_one_and_update(
                {"Email": email},
                update={
                    "$set": {"Password": self.hash_password(pwd)},
                    "$unset": {"verif_code": "", "timestamp_created": ""},
                    "$push": {"Notes": msg},
                },
            )
            return True

        raise InvalidVerificationError("Incorrect Verification Code")


class ContactUsData:
    def __init__(self) -> None:
        """
        Connect to MongoDB
        """
        client = pymongo.MongoClient(DATABASE["mongo_uri"])
        self.db = client[DATABASE["db"]][os.getenv("CONTACT_US_DATA_COLLECTION")]

    def generate_query_id(self) -> str:
        """Generates a unique query id

        Args:
            None

        Returns:
            str
        """
        q_id = "".join(
            random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits
            )
            for _ in range(16)
        )
        q_id = "query_" + q_id

        if self.db.find_one({"query_id": q_id}):
            q_id = self.generate_query_id()
        return q_id

    def validate_query_id(self, qid: str) -> bool:
        """Validates query id for particular user

        Args:
            qid: Query ID

        Returns:
            bool
        """
        value = self.db.find_one({"query_id": qid})
        if value:
            return True

        raise InvalidQIDError(f"Query With query_id {qid} NOT Found")

    def insert_contact_us_data(self, name: str, email: str, message: str, status: str) -> bool:
        """Inserts Contact Us Data & Updates User Profile With Query ID

        Args:
            name: Name of User
            email: User Email ID
            message: Contact Us Message
            status: Status of Query

        Returns:
            bool
        """
        data = {
            "query_id": self.generate_query_id(),
            "Name": name,
            "Email": email,
            "Message": message,
            "Status": status,
        }

        try:
            self.db.insert_one(data)

            # UPDATE USER CONTACTUS[] WITH QUERY ID

            return True
        except Exception:
            raise ContactUsDataInsertionError("Error Inserting Contact Us Data")
