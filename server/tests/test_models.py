from dotenv import load_dotenv
import requests
import unittest
import pymongo
import os

from core.settings import DATABASE
from mainapp.errors import (
    FileAlreadyExistsForCurrentUserError,
    FileDoesNotExistForCurrentUserError,
    DataFetchingError,
)
from mainapp import (
    S3_Functions,
    Music_Data,
)
from . import Base

data = Base()


class TestClient(unittest.TestCase):
    """
    Integration tests
    """

    @classmethod
    def setUpClass(cls) -> None:

        load_dotenv()

        cls.client = requests.Session()
        cls.pymongo_client = pymongo.MongoClient(DATABASE["mongo_uri"])
        cls.db = cls.pymongo_client[DATABASE["db"]][os.getenv("DATA_COLLECTION")]
        cls.api_url = "http://localhost:8000/api/data"

    def test_file_exists(self):
        response = self.client.post(
            url=self.api_url,
            data=data.test_data,
        )

        self.assertEqual(response.status_code, 200)

        with self.assertRaises(FileAlreadyExistsForCurrentUserError):
            Music_Data.insert_data(
                data.test_data["Name"],
                data.test_data["Email"],
                data.test_data["Filename"],
                data.test_data["CloudFilename"],
            )

        self.clean()

    def test_file_not_exists(self):
        with self.assertRaises(FileDoesNotExistForCurrentUserError):
            Music_Data.delete_data(
                data.wrong_data["wrong_email"], data.wrong_data["wrong_file"]
            )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.db.delete_many({})
        cls.pymongo_client.close()
        cls.client.close()

    def clean(self):
        self.db.delete_many({})
        try:
            S3_Functions.delete_file_from_s3(data.test_data["CloudFilename"])
        except Exception as e:
            print("Deletion Error")
