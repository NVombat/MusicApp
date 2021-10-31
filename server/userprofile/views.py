from rest_framework.views import APIView
from django.http import response

from .utils import send_profile_data
from core.throttle import throttle


class Profile(APIView):
    throttle_classes = [throttle]

    def get(self, request, **kwargs) -> response.JsonResponse:
        """Sending specific user data when hit with GET requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """

        print("Sending Profile Data API")

        data = send_profile_data(request, **kwargs)

        return data
