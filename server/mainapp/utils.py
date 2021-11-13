from rest_framework import status
from django.http import response
import datetime as d

from core.settings import AWS_BUCKET_FOLDER, AWS_OBJECT_URL_PREFIX
from .errors import (
    FileAlreadyExistsForCurrentUserError,
    DataFetchingError,
    AWSDownloadError,
)
from . import S3_Functions, Music_Data


def recv_music_data(request, **kwargs) -> response.JsonResponse:
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
        objectURL = AWS_OBJECT_URL_PREFIX + cloudFilename

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


def send_music_data(request, **kwargs) -> response.JsonResponse:
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
            status=status.HTTP_404_NOT_FOUND,
        )
    except Exception as e:
        return response.JsonResponse(
            {"error": "Error Occured While Sending Data", "success_status": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
