from dotenv import load_dotenv
import requests
import unittest
import pymongo
import os

from core.settings import DATABASE
from mainapp.errors import (
    FileAlreadyExistsForCurrentUserError,
    FileDoesNotExistForCurrentUserError,
)
from mainapp import (
    S3_Functions,
    Music_Data,
)
from mainapp.models import Likes, Comments
from . import Base

data = Base()


class TestAppModels(unittest.TestCase):
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
        cls.c_db = cls.pymongo_client[DATABASE["db"]][
            os.getenv("CONTACT_US_DATA_COLLECTION")
        ]
        cls.api_upload_url = "http://localhost:8000/api/app/uploads"
        cls.api_posts_url = "http://localhost:8000/api/app/posts"

    def test_file_exists(self):
        try:
            response = self.client.post(
                url=self.api_upload_url,
                data=data.test_data,
            )

            self.assertEqual(response.status_code, 200)

        except requests.exceptions.ConnectionError:
            print("Connection Error")

        # with self.assertRaises(FileAlreadyExistsForCurrentUserError):
        #     Music_Data.insert_data(
        #         data.test_data["Date"],
        #         data.test_data["Name"],
        #         data.test_data["Email"],
        #         data.test_data["Filename"],
        #         data.test_data["CloudFilename"],
        #         data.test_data["ObjectURL"],
        #     )

    def test_comments_functionality(self):
        com = Comments()
        com.delete_all_data()
        com.insert_data(data.comment_data["music_data_pid"], data.comment_data["user_email"], data.comment_data["comment"])
        fetched_data = com.fetch_data()
        self.assertDictEqual(fetched_data[0], data.comment_data)
        com.delete_data(data.comment_data["comment"])
        fetched_data = com.fetch_data()
        self.assertListEqual(fetched_data, [])

    def test_likes_functionality(self):
        like = Likes()
        like.delete_all_data()
        like.insert_data(data.like_data["music_data_pid"], data.like_data["user_email"])
        fetched_data = like.fetch_data()
        self.assertDictEqual(fetched_data[0], data.like_data)
        like.delete_data(data.like_data["music_data_pid"], data.like_data["user_email"])
        fetched_data = like.fetch_data()
        self.assertListEqual(fetched_data, [])

    def test_file_not_exists(self):
        with self.assertRaises(FileDoesNotExistForCurrentUserError):
            Music_Data.delete_data(
                data.wrong_data["wrong_email"], data.wrong_data["wrong_file"]
            )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.m_db.remove({})
        cls.u_db.remove({})
        cls.c_db.remove({})
        cls.pymongo_client.close()
        cls.client.close()
        try:
            S3_Functions.delete_file_from_s3(data.test_data["CloudFilename"])
        except Exception:
            print("Deletion Error")

    def clean(self):
        self.m_db.remove({})
        self.u_db.remove({})
        self.c_db.remove({})
        try:
            S3_Functions.delete_file_from_s3(data.test_data["CloudFilename"])
        except Exception:
            print("Deletion Error")
