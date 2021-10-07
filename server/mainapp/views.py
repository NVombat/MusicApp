from django.http.response import JsonResponse
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import status
from django.http import response
import requests

from .utils import music_data_upload
from mainapp import Music_Data


class Upload(APIView):
    def post(self, request, **kwargs) -> JsonResponse:

        print("CHECKING API")
        print("REQUEST DATA:", request.data)
        # music_data_upload(request)

        return response.JsonResponse(
            data={"response": "true"}, status=status.HTTP_200_OK
        )

    def get(self, request, **kwargs):
        """
        Backend will be uploading data (sending)
        """
        return response.JsonResponse(data={"response": "true"})
