from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import response

from .utils import recv_music_data, send_music_data
from core.throttle import throttle


class Uploads(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [throttle]

    def post(self, request, **kwargs) -> response.JsonResponse:
        """Receiving user uploaded data via POST requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """

        print("Receiving Data API")

        upload_data = recv_music_data(request, **kwargs)

        return upload_data


class Posts(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [throttle]

    def get(self, request, **kwargs) -> response.JsonResponse:
        """Sending user data when hit with GET requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """

        print("Sending Data API")

        post_data = send_music_data(request, **kwargs)

        return post_data
