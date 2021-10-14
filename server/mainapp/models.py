from django.http.response import JsonResponse
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
        self, name: str, email: str, filename: str, cloud_filename: str
    ) -> None:
        """Insert file name and data into db

        Args:
            name: User Name
            email: User Email ID
            filename: Name of File
            cloud_filename: Name/Path of file in S3

        Returns:
            None
        """
        if self.db.find_one({"Email": email, "Filename": filename}):
            raise FileAlreadyExistsForCurrentUserError(
                "File Already Exists With This Name For Current User"
            )

        data = {
            "Name": name,
            "Email": email,
            "Filename": filename,
            "CloudFilename": cloud_filename,
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
        ):
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


# md = MusicData()
# try:
#     md.insert_data("Nikhill Vombatkere", "nv9824@srmist.edu.in", "stay.mp3", "files/nv9824/stay.mp3")
#     md.insert_data("Aradhya Tripathi", "at5079@srmist.edu.in", "hello.mp3", "files/at5079/hello.mp3")
#     md.insert_data("Sanah Sidhu", "ss6153@srmist.edu.in", "dream.mp3", "files/ss6153/dream.mp3")
#     md.insert_data("Nikhill Vombatkere", "nv9824@srmist.edu.in", "done.mp3", "files/nv9824/done.mp3")
# except FileAlreadyExistsForCurrentUserError as e:
#     print("Error:", str(e))

# try:
#     md.delete_data("nv9824@srmist.edu.in", "done.mp3")
# except FileDoesNotExistForCurrentUserError as e:
#     print("Error:", str(e))

# print(md.fetch_data())
