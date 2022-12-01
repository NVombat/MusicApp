from authentication import validate
from core.throttle import throttle
from django.http import response
from rest_framework.views import APIView

from .utils import delete_profile_data, send_profile_data


class Profile(APIView):
    # permission_classes = [validate.ValidateUser]
    throttle_classes = [throttle]

    def get(self, request, **kwargs) -> response.JsonResponse:
        """Sending specific user data when hit with GET requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """
        profile_data = send_profile_data(request, **kwargs)

        return profile_data

    def delete(self, request, **kwargs) -> response.JsonResponse:
        """Deleting specific user data when hit with DELETE requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """
        delete_data = delete_profile_data(request, **kwargs)

        return delete_data
