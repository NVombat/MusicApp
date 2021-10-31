from dotenv import load_dotenv
import requests
import unittest
import pymongo
import os

from core.settings import DATABASE
from mainapp import S3_Functions
from . import Base

data = Base()


class TestAPI(unittest.TestCase):
    """
    Integration tests
    """

    @classmethod
    def setUpClass(cls) -> None:

        load_dotenv()

        cls.client = requests.Session()
        cls.pymongo_client = pymongo.MongoClient(DATABASE["mongo_uri"])
        cls.db = cls.pymongo_client[DATABASE["db"]][os.getenv("DATA_COLLECTION")]
        cls.api_upload_url = "http://localhost:8000/api/uploads"
        cls.api_posts_url = "http://localhost:8000/api/posts"
        cls.api_profile_url = "http://localhost:8000/api/profile"

    def test_data_recv(self):
        response = self.client.post(
            url=self.api_upload_url,
            data=data.test_data,
        )
        self.assertEqual(response.status_code, 200)

    def test_data_send(self):
        response = self.client.get(self.api_posts_url)
        self.assertEqual(response.status_code, 200)

    def test_user_data_send(self):
        response = self.client.get(self.api_profile_url)
        self.assertEqual(response.status_code, 200)

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
        cls.db.delete_many({})
        cls.pymongo_client.close()
        cls.client.close()
        try:
            S3_Functions.delete_file_from_s3(data.test_data["CloudFilename"])
        except Exception as e:
            print("Deletion Error")

    def clean(self):
        self.db.delete_many({})
        try:
            S3_Functions.delete_file_from_s3(data.test_data["CloudFilename"])
        except Exception as e:
            print("Deletion Error")
