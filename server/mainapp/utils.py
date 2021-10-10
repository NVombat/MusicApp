from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.http import response
import requests

from core.settings import AWS_BUCKET_FOLDER
from .errors import (
    FileAlreadyExistsForCurrentUserError,
    DataFetchingError,
    AWSDownloadError,
)

from . import S3_Functions, Music_Data


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

        filename = filename.lower()
        subfolder = email.split("@")[0]
        cloudFilename = AWS_BUCKET_FOLDER + subfolder + "/" + filename

        Music_Data.insert_data(name, email, filename, cloudFilename)

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
        record["success_status"] = True
        print(record)

        return response.JsonResponse(record, status=status.HTTP_200_OK)

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
