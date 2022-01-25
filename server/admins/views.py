from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.http import response

from .utils import delete_music_data, send_music_data, login_admin
from core.throttle import throttle
from . import validate_admins


class AdminLogin(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = [throttle]

    def post(self, request, **kwargs) -> response.JsonResponse:
        """Receiving admin login credentials via POST requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """
        print("Login Admin Post Request")

        login_data = login_admin(request, **kwargs)

        return login_data


class AdminView(APIView):
    permission_classes = [validate_admins.ValidateAdmin]
    throttle_classes = [throttle]

    def get(self, request, **kwargs) -> response.JsonResponse:
        """Sending user data when hit with GET requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """

        print("Sending Data To Admins API")

        post_data = send_music_data(request, **kwargs)

        return post_data

    def delete(self, request, **kwargs) -> response.JsonResponse:
        """Deleting specific music data when hit with DELETE requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """

        print("Deleting Data For Admins API")

        delete_data = delete_music_data(request, **kwargs)

        return delete_data
