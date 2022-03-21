from rest_framework import status
from django.http import response

from .errors import FileDoesNotExistForCurrentUserError, ProfileDataUnavailableError
from core.errors import PageDoesNotExistError
from mainapp.aws import AWSFunctionsS3
from . import User_Data, Paginate


def send_profile_data(request, **kwargs) -> response.JsonResponse:
    """Sends paginated profile data when user requests through GET requests

    Args:
        request
        **kwargs

    Returns:
        response.JsonResponse
    """
    try:
        page = int(request.query_params.get("Page"))
        email = request.query_params.get("Email")

        user_data = User_Data.fetch_user_data(email)

        return Paginate.get_paginated_data(page, user_data)

    except ProfileDataUnavailableError:
        return response.JsonResponse(
            {"error_status": True, "success_status": False},
            status=status.HTTP_404_NOT_FOUND,
        )
    except PageDoesNotExistError:
        return response.JsonResponse(
            {"error_status": True, "success_status": False},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Exception:
        return response.JsonResponse(
            {"error_status": True, "success_status": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def delete_profile_data(request, **kwargs) -> response.JsonResponse:
    """Deletes profile data when user sends DELETE requests

    Args:
        request
        **kwargs

    Returns:
        response.JsonResponse
    """
    try:
        pid = request.query_params.get("PID")
        email = request.query_params.get("Email")

        aws_s3_func = AWSFunctionsS3()
        cloud_filename = User_Data.get_cloud_filename(pid, email)
        aws_s3_func.delete_file_from_s3(cloud_filename)

        User_Data.delete_user_data(pid, email)

        return response.JsonResponse(
            {"success_status": True},
            status=status.HTTP_200_OK,
        )

    except FileDoesNotExistForCurrentUserError:
        return response.JsonResponse(
            {"error_status": True, "success_status": False},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Exception:
        return response.JsonResponse(
            {
                "error_status": True,
                "success_status": False,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
