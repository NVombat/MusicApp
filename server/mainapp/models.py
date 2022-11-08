from django.http import response
from dotenv import load_dotenv
import pymongo
import uuid
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

    def generate_id(self) -> str:
        """Generates a unique hex object id

        Args:
            None

        Returns:
            str
        """
        pid = uuid.uuid4().hex

        if self.db.find_one({"PID": pid}):
            pid = self.generate_id()
        return pid

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
                f"File With Name {filename} Already Exists For User {email}"
            )

        data = {
            "PID": self.generate_id(),
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
                f"File With Name {filename} Does Not Exist For The User {email}"
            )

    def fetch_data(self) -> response.JsonResponse:
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
            docs = list(data)
            # docs.append({"success_status": True})
            # json_data = response.JsonResponse(docs, safe=False)
            # return json_data
            return docs

        raise DataFetchingError("There Are No Posts In The Database At This Moment")


class Likes:
    def __init__(self) -> None:
        """
        Connect to MongoDB
        """
        client = pymongo.MongoClient(DATABASE["mongo_uri"])
        self.db = client[DATABASE["db"]]["Likes"]

    def insert_data(
            self,
            music_data_pid: str,
            user_email: str,
    ) -> None:
        """Insert file name and data into db

        Args:
            music_data_pid: FK for pid of the post
            user_email: FK for user email

        Returns:
            None
        """
        if self.db.find_one({"music_data_pid": music_data_pid, "user_email": user_email}):
            raise FileAlreadyExistsForCurrentUserError(
                f"Like for post {music_data_pid} Already Exists For User {user_email}"
            )

        data = {
            "music_data_pid": music_data_pid,
            "user_email": user_email,
        }
        self.db.insert_one(data)

    def delete_data(self, music_data_pid: str, user_email: str) -> None:
        """Delete file and related data from db

        Args:
            music_data_pid: User Email ID
            user_email: Name of File

        Returns:
            None
        """
        if self.db.find_one(
                {
                    "music_data_pid": music_data_pid,
                    "user_email": user_email,
                }
        ):
            self.db.delete_one(
                {
                    "music_data_pid": music_data_pid,
                    "user_email": user_email,
                },
            )
        else:
            raise FileDoesNotExistForCurrentUserError(
                f"Like for post {music_data_pid} does not exists for user {user_email}"
            )

    def delete_all_data(self) -> None:
        """Delete all likes from db

                Args:
                    None

                Returns:
                    None
                """
        self.db.remove()

    def fetch_data(self) -> response.JsonResponse:
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
        ).sort("music_data_pid", -1):
            likes = list(data)
            return likes

        raise DataFetchingError("There Are No Likes In The Database At This Moment")


class Comments:
    def __init__(self) -> None:
        """
        Connect to MongoDB
        """
        client = pymongo.MongoClient(DATABASE["mongo_uri"])
        self.db = client[DATABASE["db"]]["Comments"]

    def insert_data(
            self,
            music_data_pid: str,
            user_email: str,
            comment: str,
    ) -> None:
        """Insert coments name and data into db

        Args:
            music_data_pid: FK for pid of the post
            user_email: FK for user email
            comment: comment

        Returns:
            None
        """

        data = {
            "music_data_pid": music_data_pid,
            "user_email": user_email,
            "comment": comment,
        }
        self.db.insert_one(data)

    def delete_data(self, comment_id: str) -> None:
        """Delete comment

        Args:
            comment_id: comment ID

        Returns:
            None
        """
        if self.db.find_one(
                {
                    "_id": comment_id,
                }
        ):
            self.db.delete_one(
                {
                    "_id": comment_id,
                },
            )
        else:
            raise FileDoesNotExistForCurrentUserError(
                f"Comment with id {comment_id} does not exists."
            )

    def delete_all_data(self) -> None:
        """Delete all comments

                Args:
                    None

                Returns:
                    None
                """
        self.db.remove()

    def fetch_data(self) -> response.JsonResponse:
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
        ).sort("music_data_pid", -1):
            comments = list(data)
            return comments

        raise DataFetchingError("There Are No Likes In The Database At This Moment")
