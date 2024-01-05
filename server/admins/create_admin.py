import binascii
import hashlib
import os
import random
import string

import pymongo
from dotenv import load_dotenv

load_dotenv()


def generate_admin_id(db) -> str:
    """Generates a unique admin id

    Args:
        db: db connection object

    Returns:
        str
    """
    admin_id = "".join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
        for _ in range(16)
    )
    admin_id = "adm_" + admin_id

    if db.find_one({"user_id": admin_id}):
        admin_id = generate_admin_id(db)
    return admin_id


def hash_password(pwd: str) -> str:
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


def generate_admin(name: str, email: str, pwd: str) -> None:
    """Creates an admin user entry in the database

    Args:
        name: Admin Name
        email: Admin Email
        pwd: Admin Account Password

    Returns:
        None
    """
    try:
        debug = True if os.getenv("DEBUG") else False
        use_db = "MONGO" if debug is False else "TEST"

        if use_db == "MONGO":
            database = {
                "mongo_uri": os.getenv("MONGO_URI"),
                "db": os.getenv("MONGO_DB"),
            }
        elif use_db == "TEST":
            database = {
                "mongo_uri": os.getenv("TEST_MONGO_URI"),
                "db": os.getenv("TEST_MONGO_DB"),
            }

        client = pymongo.MongoClient(database["mongo_uri"])
        db = client[database["db"]][os.getenv("USER_DATA_COLLECTION")]

        if db.find_one({"Email": email}):
            raise Exception(f"Admin {email} Already Exists...")
        else:
            pwd = hash_password(pwd)
            rec = {
                "user_id": generate_admin_id(db),
                "Username": name,
                "Email": email,
                "Password": pwd,
            }
            db.insert_one(rec)
    except Exception:
        print("Error Generating Admin...")


if __name__ == "__main__":
    name = input("Enter Admin Name: ")
    email = input("Enter Admin Email ID: ")
    pwd = input("Enter Admin Password: ")

    try:
        generate_admin(name, email, pwd)
        print("Admin Created Successfully...")
    except Exception:
        print("Error Creating Admin... Try Again...")
