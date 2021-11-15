from dotenv import load_dotenv
import requests
import unittest
import pymongo
import os

from core.settings import DATABASE


class Test_Auth_Model(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:

        load_dotenv()

        cls.client = requests.Session()
        cls.pymongo_client = pymongo.MongoClient(DATABASE["mongo_uri"])
        cls.db = cls.pymongo_client[DATABASE["db"]][os.getenv("USER_DATA_COLLECTION")]
