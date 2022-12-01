import os

import pymongo
from core.settings import DATABASE
from django.http import response
from dotenv import load_dotenv

from .errors import (FileDoesNotExistForCurrentUserError,
                     ProfileDataUnavailableError)

load_dotenv()


class UserData:
    def __init__(self) -> None:
        """
        Connect to MongoDB
        """
        client = pymongo.MongoClient(DATABASE["mongo_uri"])
        self.db = client[DATABASE["db"]][os.getenv("DATA_COLLECTION")]

    def get_cloud_filename(self, pid: str, email: str) -> str:
        """Fetches cloud filename

        Args:
            pid: PID of File
            email: Email of user

        Returns:
            str
        """
        if value := self.db.find_one(
            {
                "PID": pid,
                "Email": email,
            }
        ):
            cloudfilename = value["CloudFilename"]
            return cloudfilename
        else:
            raise FileDoesNotExistForCurrentUserError(
                f"File With ID {pid} Does Not Exist For The User {email}"
            )

    def fetch_user_data(self, email: str) -> response.JsonResponse:
        """Fetches specific user data from db

        Args:
            email: Email of user

        Returns:
            response.JsonResponse
        """
        if data := self.db.find(
            {"Email": email},
            {
                "_id": 0,
            },
        ):
            data.sort("Date", -1)
            docs = list(data)
            # docs.append({"success_status": True})
            # json_data = response.JsonResponse(docs, safe=False)
            # return json_data
            return docs

        raise ProfileDataUnavailableError(f"The User, {email}, Does Not Have Any Posts")

    def delete_user_data(self, pid: str, email: str) -> None:
        """Delete specific user file from db

        Args:
            pid: Object ID
            email: User Email ID

        Returns:
            None
        """
        if self.db.find_one(
            {
                "PID": pid,
                "Email": email,
            }
        ):
            self.db.delete_one(
                {
                    "PID": pid,
                    "Email": email,
                },
            )
        else:
            raise FileDoesNotExistForCurrentUserError(
                f"File With ID {pid} Does Not Exist For The User {email}"
            )
