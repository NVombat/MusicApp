from django.http.response import JsonResponse
from rest_framework.response import Response
from boto3.session import Session
from rest_framework import status
from django.http import response
import requests

from core.settings import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_STORAGE_BUCKET_NAME,
)
from .errors import DataFetchingError, FileAlreadyExistsForCurrentUserError
from . import Music_Data


def recv_music_data(request, **kwargs):
    try:
        print("Request Object DATA:", request.data)

        name = request.data.get("Name")
        email = request.data.get("Email")
        filename = request.data.get("Filename")
        uploadedFile = request.data.get("File")

        filename = filename.lower()
        subfolder = email.split("@")[0]
        cloudFilename = "files/" + subfolder + "/" + filename

        Music_Data.insert_data(name, email, filename, cloudFilename)

        try:
            session = Session(
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            )
            s3 = session.resource("s3")
            s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
                Key=cloudFilename, Body=uploadedFile
            )

        except Exception as e:
            return response.JsonResponse(
                {"error": "AWS File Upload Error", "success_status": False},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        return response.JsonResponse(
            {"success_status": True},
            status=status.HTTP_200_OK,
        )

    except FileAlreadyExistsForCurrentUserError as fae:
        return response.JsonResponse(
            {"error": str(fae), "success_status": False},
            status=status.HTTP_400_BAD_REQUEST,
        )
    except Exception as e:
        return response.JsonResponse(
            {"error": "Error Occured While Receiving Data", "success_status": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def send_music_data(request, **kwargs):
    try:
        data = Music_Data.fetch_data()
        return response.JsonResponse(data=data, status=status.HTTP_200_OK)

    except Exception as e:
        return response.JsonResponse(
            {"error": "Error Occured While Sending Data"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    except DataFetchingError as dfe:
        return response.JsonResponse(
            {"error": str(dfe)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
