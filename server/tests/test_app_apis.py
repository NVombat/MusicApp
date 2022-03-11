from dotenv import load_dotenv
import requests
import unittest
import pymongo
import json
import os

from .base_user import CustomUserTests
from core.settings import DATABASE
from mainapp import S3_Functions
from . import Base

user = CustomUserTests()
data = Base()


class TestAppAPI(unittest.TestCase):
    """
    Integration tests
    """

    @classmethod
    def setUpClass(cls) -> None:

        load_dotenv()

        cls.client = requests.Session()
        cls.pymongo_client = pymongo.MongoClient(DATABASE["mongo_uri"])
        cls.m_db = cls.pymongo_client[DATABASE["db"]][os.getenv("DATA_COLLECTION")]
        cls.u_db = cls.pymongo_client[DATABASE["db"]][os.getenv("USER_DATA_COLLECTION")]
        cls.c_db = cls.pymongo_client[DATABASE["db"]][os.getenv("CONTACT_US_DATA_COLLECTION")]

        cls.api_upload_url = "http://localhost:8000/api/app/uploads"
        cls.api_posts_url = "http://localhost:8000/api/app/posts"
        cls.api_contactus_url = "http://localhost:8000/api/app/contactus"

        cls.api_profile_url = "http://localhost:8000/api/user/profile"

    def test_uploads(self):
        tokens = user.login_user()
        acc_tok = tokens["access_token"]

        user.headers.update({"Authorization": f"Bearer {acc_tok}"})
        response = self.client.post(
            url=self.api_upload_url,
            data=data.test_data,
            headers=user.headers,
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            url=self.api_upload_url,
            data=data.test_data,
            headers=user.headers,
        )
        self.assertEqual(response.status_code, 400)

        response = self.client.post(
            url=self.api_upload_url,
            data=data.incomplete_data,
            headers=user.headers,
        )
        self.assertEqual(response.status_code, 500)

    def test_posts(self):
        response = self.client.get(self.api_posts_url + "?Page=1")
        self.assertEqual(response.status_code, 200)

        response = self.client.get(self.api_posts_url + "?Page=1000")
        self.assertEqual(response.status_code, 404)

        response = self.client.get(self.api_posts_url)
        self.assertEqual(response.status_code, 500)

    def test_contact_us(self):
        tokens = user.login_user()

        response = self.client.post(
            url=self.api_contactus_url,
            data=data.contact_us_data,
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            url=self.api_contactus_url,
            data=data.wrong_contact_us_data,
        )
        self.assertEqual(response.status_code, 500)

        response = self.client.post(
            url=self.api_contactus_url,
            data=data.incomplete_data,
        )
        self.assertEqual(response.status_code, 500)

    def test_user_profile_data(self):
        tokens = user.login_user()
        acc_tok = tokens["access_token"]

        user.headers.update({"Authorization": f"Bearer {acc_tok}"})
        response = self.client.get(
            url=self.api_profile_url + "?Email=test@gmail.com&Page=1",
            headers=user.headers,
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            url=self.api_profile_url + "?Email=wrong@gmail.com&Page=1",
            headers=user.headers,
        )
        self.assertEqual(response.status_code, 404)

        response = self.client.get(
            url=self.api_profile_url + "?Email=test@gmail.com&Page=1000",
            headers=user.headers,
        )
        self.assertEqual(response.status_code, 404)

        response = self.client.get(
            url=self.api_profile_url,
            headers=user.headers,
        )
        self.assertEqual(response.status_code, 500)

        response = self.client.delete(
            url=self.api_profile_url + "?Email=test@gmail.com&PID=abc",
            headers=user.headers,
        )
        self.assertEqual(response.status_code, 404)

        response = self.client.delete(
            url=self.api_profile_url,
            headers=user.headers,
        )
        self.assertEqual(response.status_code, 500)

    def test_fail_post(self):
        response = self.client.post(
            url=self.api_posts_url,
            data=data.test_data,
        )
        # Method not allowed
        self.assertEqual(response.status_code, 405)

    def test_fail_get(self):
        response = self.client.get(self.api_upload_url)
        # Method not allowed
        self.assertEqual(response.status_code, 405)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.m_db.remove({})
        cls.u_db.remove({})
        cls.c_db.remove({})
        cls.pymongo_client.close()
        cls.client.close()
        try:
            S3_Functions.delete_file_from_s3(data.test_data["CloudFilename"])
        except Exception as e:
            print("Deletion Error")

    def clean(self):
        self.m_db.remove({})
        self.u_db.remove({})
        self.c_db.remove({})
        try:
            S3_Functions.delete_file_from_s3(data.test_data["CloudFilename"])
        except Exception as e:
            print("Deletion Error")

    def tearDown(self) -> None:
        user.cleanup()
