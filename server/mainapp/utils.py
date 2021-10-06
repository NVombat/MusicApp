from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.http import response

from .errors import FileAlreadyExistsForCurrentUserError
from . import Music_Data


def music_data(request, **kwargs):
    try:
        name = request.GET["Name"]
        email = request.GET["Email"]
        filename = request.GET["Filename"]

        Music_Data.insert_data(name, email, filename)

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
            {"error": "Error Occured While Receiving Data"}, status=status.HTTP_400_BAD_REQUEST
        )
