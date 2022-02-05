from dotenv import load_dotenv
from unittest import TestCase
import requests
import pymongo
import json
import os

from core.settings import DATABASE

load_dotenv()


class CustomUserTests(TestCase):
    request = requests.Session()
    base_url = "http://localhost:8000/api/"
    headers = {"Content-Type": "application/json"}
    client = pymongo.MongoClient(DATABASE["mongo_uri"])
    db = client[DATABASE["db"]][os.getenv("USER_DATA_COLLECTION")]

    def user_data(
        self,
        username: str = "testuser",
        email: str = "test@gmail.com",
        password: str = "testpwd",
    ):
        record = {
            "Username": username,
            "Email": email,
            "Password": password,
        }

        return record

    def login_user(self, get_refresh=False):
        user_data = self.user_data()

        response = self.request.post(
            self.base_url + "auth/register",
            data=json.dumps(user_data),
            headers=self.headers,
        )
        self.assertEqual(response.status_code, 201)

        login_response = self.request.post(
            self.base_url + "auth/login",
            data=json.dumps(
                {"Email": user_data["Email"], "Password": user_data["Password"]}
            ),
            headers=self.headers,
        )
        self.assertEqual(login_response.status_code, 200)

        tokens = login_response.json()
        if get_refresh:
            return tokens
        return tokens["access_token"]

    def admin_data(
        self, email: str = "testadmin@gmail.com", password: str = "adminpwd"
    ):
        adm_record = {
            "Email": email,
            "Password": password,
        }

        return adm_record

    def login_admin(self, get_refresh=False):
        adm_data = self.admin_data()

        login_response = self.request.post(
            self.base_url + "admin/login",
            data=json.dumps(
                {"Email": adm_data["Email"], "Password": adm_data["Password"]}
            ),
            headers=self.headers,
        )
        self.assertEqual(login_response.status_code, 200)

        tokens = login_response.json()
        if get_refresh:
            return tokens
        return tokens["access_token"]

    def cleanup(self):
        self.db.drop_collection("UserData")
