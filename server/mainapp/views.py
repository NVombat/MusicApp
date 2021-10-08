from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from django.http import response
import requests

from .utils import recv_music_data, send_music_data


class Data(APIView):
    def post(self, request, **kwargs) -> JsonResponse:
        """Receiving user uploaded data via POST requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """

        print("Receiving Data API")

        data = recv_music_data(request, **kwargs)

        return data

    def get(self, request, **kwargs) -> JsonResponse:
        """Sending user data when hit with GET requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """

        print("Sending Data API")

        data = send_music_data(request, **kwargs)

        return data
