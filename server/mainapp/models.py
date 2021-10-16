from django.http import response
from dotenv import load_dotenv
import pymongo
import os

from core.settings import DATABASE

from .errors import (
    FileAlreadyExistsForCurrentUserError,
    FileDoesNotExistForCurrentUserError,
    DataFetchingError,
)

load_dotenv()


class MusicData:
    def __init__(self) -> None:
        """
        Connect to MongoDB
        """
        client = pymongo.MongoClient(DATABASE["mongo_uri"])
        self.db = client[DATABASE["db"]][os.getenv("DATA_COLLECTION")]

    def insert_data(
        self,
        date: str,
        name: str,
        email: str,
        filename: str,
        cloud_filename: str,
        object_url: str,
    ) -> None:
        """Insert file name and data into db

        Args:
            name: User Name
            email: User Email ID
            filename: Name of File
            cloud_filename: Name/Path of file in S3
            object_url: URL of object in S3

        Returns:
            None
        """
        if self.db.find_one({"Email": email, "Filename": filename}):
            raise FileAlreadyExistsForCurrentUserError(
                "File Already Exists With This Name For Current User"
            )

        data = {
            "Date": date,
            "Name": name,
            "Email": email,
            "Filename": filename,
            "CloudFilename": cloud_filename,
            "ObjectURL": object_url,
        }
        self.db.insert_one(data)

    def delete_data(self, email: str, filename: str) -> None:
        """Delete file and related data from db

        Args:
            email: User Email ID
            filename: Name of File

        Returns:
            None
        """
        if self.db.find_one(
            {
                "Email": email,
                "Filename": filename,
            }
        ):
            self.db.delete_one(
                {
                    "Email": email,
                    "Filename": filename,
                },
            )
        else:
            raise FileDoesNotExistForCurrentUserError(
                "File Does Not Exist For The Current User"
            )

    def fetch_data(self) -> dict:
        """Fetches all data from db

        Args:
            None

        Returns:
            response.JsonResponse
        """
        if data := self.db.find(
            {},
            {
                "_id": 0,
            },
        ).sort("Date", -1):
            # data_response = {}

            # cnt = 1
            # for val in data:
            #     data_response[str(cnt)] = val
            #     cnt = cnt + 1

            # return data_response

            docs = list(data)
            # docs.append({"success_status": True})

            json_data = response.JsonResponse(docs, safe=False)
            return json_data

        raise DataFetchingError("Error While Fetching Data")
