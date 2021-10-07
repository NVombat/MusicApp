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
from .errors import FileAlreadyExistsForCurrentUserError
from . import Music_Data


def music_data_upload(request, **kwargs):
    try:
        print(request.data)
        name = request.data.get("Name")
        email = request.data.get("Email")
        filename = request.data.get("Filename")
        uploadedFile = request.data.get("File")

        cloudFilename = "files/" + filename

        Music_Data.insert_data(name, email, filename)

        session = Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )
        s3 = session.resource("s3")
        s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
            Key=cloudFilename, Body=uploadedFile
        )

        return response.JsonResponse(
            {
                "Name": name,
                "Email": email,
                "Filename": filename,
            },
            status=status.HTTP_200_OK,
        )

    except FileAlreadyExistsForCurrentUserError as e:
        return response.JsonResponse(
            {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        return response.JsonResponse(
            {"error": "Error Occured While Receiving Data"},
            status=status.HTTP_400_BAD_REQUEST,
        )


def music_data(request, **kwargs):
    try:
        url = ""
        filename = ""
        files = {"file": open(filename, "rb")}
        r = requests.post(url, files=files)

    except Exception as e:
        return response.JsonResponse(
            {"error": "Error Occured While Sending Data"},
            status=status.HTTP_400_BAD_REQUEST,
        )
