from django.http import response
from dotenv import load_dotenv
import pymongo
import os

from core.settings import DATABASE

from .errors import (
    FileDoesNotExistForCurrentUserError,
    ProfileDataUnavailableError,
)

load_dotenv()


class UserData:
    def __init__(self) -> None:
        """
        Connect to MongoDB
        """
        client = pymongo.MongoClient(DATABASE["mongo_uri"])
        self.db = client[DATABASE["db"]][os.getenv("DATA_COLLECTION")]

    def fetch_user_data(self, email) -> response.JsonResponse:
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
            json_data = response.JsonResponse(docs, safe=False)
            return json_data

        raise ProfileDataUnavailableError(f"The User, {email}, Does Not Have Any Posts")

    def delete_user_data(self, id: str, email: str) -> None:
        """Delete specific user file from db

        Args:
            id: Object id
            email: User Email ID

        Returns:
            None
        """
        if self.db.find_one(
            {
                "ID": id,
                "Email": email,
            }
        ):
            self.db.delete_one(
                {
                    "ID": id,
                    "Email": email,
                },
            )
        else:
            raise FileDoesNotExistForCurrentUserError(
                f"File With ID {id} Does Not Exist For The User {email}"
            )
