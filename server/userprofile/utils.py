from rest_framework import status
from django.http import response
from dotenv import load_dotenv

from .errors import ProfileDataUnavailableError
from . import User_Data

load_dotenv()


def send_profile_data(request, **kwargs) -> response.JsonResponse:
    """Sends profile data when user requests through GET requests

    Args:
        request
        **kwargs

    Returns:
        response.JsonResponse
    """
    try:
        print("USER DATA GET REQUEST")
        email = request.data.get("Email")
        print(email)

        user_data = User_Data.fetch_user_data(email)
        return user_data

    except ProfileDataUnavailableError as pde:
        return response.JsonResponse(
            {"error": str(pde), "success_status": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    except Exception as e:
        return response.JsonResponse(
            {"error": "Error Occured While Sending User Data", "success_status": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
