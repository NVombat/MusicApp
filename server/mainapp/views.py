from authentication import validate
from core.throttle import throttle
from django.http import response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .utils import recv_contact_us_data, recv_music_data, send_music_data


class Uploads(APIView):
    # permission_classes = [validate.ValidateUser]
    throttle_classes = [throttle]

    def post(self, request, **kwargs) -> response.JsonResponse:
        """Receiving user uploaded data via POST requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """
        upload_data = recv_music_data(request, **kwargs)

        return upload_data


class Posts(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = [throttle]

    def get(self, request, **kwargs) -> response.JsonResponse:
        """Sending user data when hit with GET requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """
        post_data = send_music_data(request, **kwargs)

        return post_data


class Contact_Us(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = [throttle]

    def post(self, request, **kwargs) -> response.JsonResponse:
        """Sending Contact Us data when hit with POST requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """
        contact_us_data = recv_contact_us_data(request, **kwargs)

        return contact_us_data
