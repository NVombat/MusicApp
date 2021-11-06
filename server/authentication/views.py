from rest_framework.views import APIView
from django.http import response

from .utils import register_user, login_user, reset_pwd
from core.throttle import throttle


class Register(APIView):
    throttle_classes = [throttle]

    def post(self, request, **kwargs) -> response.JsonResponse:
        """Receiving user registration data via POST requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """
        print("Register Post Request")

        data = register_user(request, **kwargs)

        return data


class Login(APIView):
    throttle_classes = [throttle]

    def post(self, request, **kwargs) -> response.JsonResponse:
        """Receiving user login credentials via POST requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """
        print("Login Post Request")

        data = login_user(request, **kwargs)

        return data


class ResetPassword(APIView):
    throttle_classes = [throttle]

    def post(self, request, **kwargs) -> response.JsonResponse:
        """Receiving user uploaded data via POST requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """
        print("Reset Password Post Request")
