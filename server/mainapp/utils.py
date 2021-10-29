from rest_framework import status
from django.http import response
from dotenv import load_dotenv
import datetime as d
import os

from core.settings import AWS_BUCKET_FOLDER
from .errors import (
    FileAlreadyExistsForCurrentUserError,
    ProfileDataUnavailableError,
    DataFetchingError,
    AWSDownloadError,
)

from . import S3_Functions, Music_Data

load_dotenv()


def recv_music_data(request, **kwargs):
    """Handles data when user uploads through POST requests

    Args:
        request
        **kwargs

    Returns:
        response.JsonResponse
    """
    try:
        print("POST REQUEST")
        print("Request Object DATA:", request.data)

        name = request.data.get("Name")
        email = request.data.get("Email")
        filename = request.data.get("Filename")
        uploadedFile = request.data.get("File")

        print(name, email, filename, uploadedFile)

        date = d.datetime.now()
        date = date.strftime("%m/%d/%Y, %H:%M:%S")
        filename = filename.lower()
        subfolder = email.split("@")[0]
        cloudFilename = AWS_BUCKET_FOLDER + subfolder + "/" + filename
        objectURL = os.getenv("AWS_S3_OBJECT_URL_PREFIX") + cloudFilename

        Music_Data.insert_data(date, name, email, filename, cloudFilename, objectURL)

        S3_Functions.upload_file_to_s3(cloudFilename, uploadedFile)

        return response.JsonResponse(
            {"success_status": True},
            status=status.HTTP_200_OK,
        )

    except FileAlreadyExistsForCurrentUserError as fae:
        return response.JsonResponse(
            {"error": str(fae), "success_status": False},
            status=status.HTTP_400_BAD_REQUEST,
        )
    except AWSDownloadError as ade:
        return response.JsonResponse(
            {"error": str(ade), "success_status": False},
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
        )
    except Exception as e:
        print(e)
        return response.JsonResponse(
            {"error": "Error Occured While Receiving Data", "success_status": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def send_music_data(request, **kwargs):
    """Sends data when user requests through GET requests

    Args:
        request
        **kwargs

    Returns:
        response.JsonResponse
    """
    try:
        print("GET REQUEST")

        record = Music_Data.fetch_data()
        # record["success_status"] = True
        # print(record)

        # return response.JsonResponse(record, status=status.HTTP_200_OK)
        return record

    except DataFetchingError as dfe:
        return response.JsonResponse(
            {"error": str(dfe), "success_status": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    except Exception as e:
        return response.JsonResponse(
            {"error": "Error Occured While Sending Data", "success_status": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def send_profile_data(request, **kwargs):
    """Sends profile data when user requests through GET requests

    Args:
        request
        **kwargs

    Returns:
        response.JsonResponse
    """
    try:
        print("USER DATA GET REQUEST")
        email = request.data.get("Email")
        print(email)

        user_data = Music_Data.fetch_user_data(email)
        return user_data

    except ProfileDataUnavailableError as pde:
        return response.JsonResponse(
            {"error": str(pde), "success_status": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    except Exception as e:
        return response.JsonResponse(
            {"error": "Error Occured While Sending User Data", "success_status": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
