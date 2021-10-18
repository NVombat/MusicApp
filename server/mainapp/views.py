from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from django.http import response

from .utils import recv_music_data, send_music_data
from core.throttle import throttle


class Uploads(APIView):
    throttle_classes = [throttle]

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
        """Sending dummy response for GET requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """
        print("Dummy GET Request")

        return response.JsonResponse({"dummy_status": True}, status=status.HTTP_200_OK)


class Posts(APIView):
    throttle_classes = [throttle]

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
