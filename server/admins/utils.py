from authentication.errors import InvalidTokenError
from core.errors import PageDoesNotExistError
from django.http import response
from mainapp.aws import AWSFunctionsS3
from mainapp.errors import DataFetchingError
from rest_framework import status
from userprofile.errors import FileDoesNotExistForCurrentUserError

from . import Admin_Auth, Admin_Token_Auth, Music_Data, Paginate, User_Data
from .errors import (
    AdminDoesNotExistError,
    AdminTokenGenerationError,
    InvalidAdminCredentialsError,
    InvalidAdminIDError,
)


def login_admin(request, **kwargs) -> response.JsonResponse:
    """Handles data when Admin Logs In through POST requests

    Args:
        request
        **kwargs

    Returns:
        response.JsonResponse
    """
    try:
        email = request.data.get("Email")
        password = request.data.get("Password")

        if Admin_Auth.check_hash(email, password):
            admin_id = Admin_Auth.get_admin_id(email)
            payload = {"aid": admin_id}

            token = Admin_Token_Auth.generate_token(
                payload=payload, expiry=1, get_refresh=True, refresh_exipry=48
            )

            return response.JsonResponse(
                data={
                    "access_token": token["access_token"],
                    "refresh_token": token["refresh_token"],
                },
                status=status.HTTP_200_OK,
            )

    except AdminDoesNotExistError:
        return response.JsonResponse(
            {"error_status": True, "auth_status": False},
            status=status.HTTP_404_NOT_FOUND,
        )
    except InvalidAdminCredentialsError:
        return response.JsonResponse(
            {"error_status": True, "auth_status": False},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    except AdminTokenGenerationError:
        return response.JsonResponse(
            {"error_status": True, "auth_status": False},
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
        )
    except Exception:
        return response.JsonResponse(
            {
                "error_status": True,
                "auth_status": False,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def send_music_data(request, **kwargs) -> response.JsonResponse:
    """Sends paginated data when admin requests through GET requests

    Args:
        request
        **kwargs

    Returns:
        response.JsonResponse
    """
    try:
        page = int(request.query_params.get("Page"))
        record = Music_Data.fetch_data()

        return Paginate.get_paginated_data(page, record)

    except DataFetchingError:
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


def delete_music_data(request, **kwargs) -> response.JsonResponse:
    """Deletes music data when Admin sends DELETE requests

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


def get_tokens(request, **kwargs) -> response.JsonResponse:
    """Verifies refresh token and generates new tokens for Admins

    Args:
        request
        **kwargs

    Returns:
        response.JsonResponse
    """
    try:
        refresh_token = request.data.get("RefreshToken")
        refresh_status = request.data.get("RefreshStatus")

        data = Admin_Token_Auth.decode_refresh_token(refresh_token)

        assert data["role"] == "admin"

        admin_id = data["aid"]

        if Admin_Auth.validate_admin_id(admin_id):
            payload = {"aid": admin_id}

            if refresh_status == "True":
                acc_token = Admin_Token_Auth.generate_token(
                    payload=payload, expiry=1, get_refresh=False
                )

                return response.JsonResponse(
                    data={
                        "access_token": acc_token,
                    },
                    status=status.HTTP_200_OK,
                )

            elif refresh_status == "False":
                token = Admin_Token_Auth.generate_token(
                    payload=payload, expiry=1, get_refresh=True, refresh_exipry=48
                )

            return response.JsonResponse(
                data={
                    "access_token": token["access_token"],
                    "refresh_token": token["refresh_token"],
                },
                status=status.HTTP_200_OK,
            )

    except InvalidTokenError:
        return response.JsonResponse(
            {"error_status": True, "success_status": False},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    except InvalidAdminIDError:
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
