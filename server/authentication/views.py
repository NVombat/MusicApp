from rest_framework.views import APIView
from django.http import response

from core.throttle import throttle


class Register(APIView):
    throttle_classes = [throttle]
    def post(self, request, **kwargs) -> response.JsonResponse:
        pass


class Login(APIView):
    throttle_classes = [throttle]

    def post(self, request, **kwargs) -> response.JsonResponse:
        pass


class ResetPassword(APIView):
    throttle_classes = [throttle]

    def post(self, request, **kwargs) -> response.JsonResponse:
        pass
