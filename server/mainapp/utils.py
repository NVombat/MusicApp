from rest_framework import status
from django.http import response
import datetime as d

from core.settings import AWS_BUCKET_FOLDER, AWS_OBJECT_URL_PREFIX
from authentication.errors import ContactUsDataInsertionError
from authentication.models import ContactUsData
from core.errors import PageDoesNotExistError
from .errors import (
    FileAlreadyExistsForCurrentUserError,
    DataFetchingError,
    AWSDownloadError,
)
from . import S3_Functions, Music_Data, Paginate

Contact_Us = ContactUsData()


def recv_music_data(request, **kwargs) -> response.JsonResponse:
    """Handles data when user uploads through POST requests

    Args:
        request
        **kwargs

    Returns:
        response.JsonResponse
    """
    try:
        name = request.data.get("Name")
        email = request.data.get("Email")
        filename = request.data.get("Filename")
        uploadedFile = request.data.get("File")

        date = d.datetime.now()
        date = date.strftime("%d/%m/%Y, %H:%M:%S")
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
    except Exception:
        return response.JsonResponse(
            {"error": "Error Occured While Receiving Data", "success_status": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def send_music_data(request, **kwargs) -> response.JsonResponse:
    """Sends paginated data when user requests through GET requests

    Args:
        request
        **kwargs

    Returns:
        response.JsonResponse
    """
    try:
        page = int(request.query_params.get("Page"))
        record = Music_Data.fetch_data()

        return Paginate.get_paginated_data(page, record)

    except DataFetchingError as dfe:
        return response.JsonResponse(
            {"error": str(dfe), "success_status": False},
            status=status.HTTP_404_NOT_FOUND,
        )
    except PageDoesNotExistError as pdne:
        return response.JsonResponse(
            {"error": str(pdne), "success_status": False},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Exception:
        return response.JsonResponse(
            {"error": "Error Occured While Sending Data", "success_status": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def recv_contact_us_data(request, **kwargs) -> response.JsonResponse:
    """Handles data when user sends feedback via contact us through POST requests

    Args:
        request
        **kwargs

    Returns:
        response.JsonResponse
    """
    try:
        name = request.data.get("Name")
        email = request.data.get("Email")
        message = request.data.get("Message")

        Contact_Us.insert_contact_us_data(name, email, message)

        return response.JsonResponse(
            {"success_status": True},
            status=status.HTTP_200_OK,
        )

    except ContactUsDataInsertionError as cdie:
        return response.JsonResponse(
            {
                "error": str(cdie),
                "success_status": True,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    except Exception:
        return response.JsonResponse(
            {
                "error": "Error Occured While Receiving Contact Us Data",
                "success_status": False,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
