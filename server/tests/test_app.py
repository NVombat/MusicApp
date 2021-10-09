from dotenv import load_dotenv
import requests
import unittest
import pymongo
import pytest
import os

from core.settings import DATABASE


class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:

        load_dotenv()

        cls.client = requests.Session()
        cls.pymongo_client = pymongo.MongoClient(DATABASE["mongo_uri"])
        cls.db = cls.pymongo_client[DATABASE["db"]][os.getenv("DATA_COLLECTION")]
        cls.base_url = "http://localhost:8000/"

    def test_models(self):
        pass
