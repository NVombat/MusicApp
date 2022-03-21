from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.http import response

from .utils import register_user, login_user, reset_pwd, reset_pwd_data, get_tokens
from core.throttle import throttle


class Register(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = [throttle]

    def post(self, request, **kwargs) -> response.JsonResponse:
        """Receiving user registration data via POST requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """
        register_data = register_user(request, **kwargs)

        return register_data


class Login(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = [throttle]

    def post(self, request, **kwargs) -> response.JsonResponse:
        """Receiving user login credentials via POST requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """
        login_data = login_user(request, **kwargs)

        return login_data


class ResetPassword(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = [throttle]

    def post(self, request, **kwargs) -> response.JsonResponse:
        """Receiving init reset data via POST requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """
        reset_data = reset_pwd(request, **kwargs)

        return reset_data


class ResetPasswordLink(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = [throttle]

    def post(self, request, **kwargs) -> response.JsonResponse:
        """Receiving reset password data via POST requests from Reset Link

        Args:
            request ([type])

        Returns:
            JsonResponse
        """
        reset_link_data = reset_pwd_data(request, **kwargs)

        return reset_link_data


class GenerateTokens(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = [throttle]

    def post(self, request, **kwargs) -> response.JsonResponse:
        """Receiving POST request to send new tokens

        Args:
            request ([type])

        Returns:
            JsonResponse
        """
        tokens = get_tokens(request, **kwargs)

        return tokens
