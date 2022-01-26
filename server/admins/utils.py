from rest_framework import status
from django.http import response

from userprofile.errors import FileDoesNotExistForCurrentUserError
from authentication.errors import InvalidTokenError
from core.errors import PageDoesNotExistError
from mainapp.errors import DataFetchingError
from .errors import (
    InvalidAdminCredentialsError,
    AdminTokenGenerationError,
    AdminDoesNotExistError,
    InvalidAdminIDError,
)

from . import Paginate, Music_Data, User_Data, Admin_Auth, Admin_Token_Auth
from mainapp.aws import AWSFunctionsS3


def login_admin(request, **kwargs) -> response.JsonResponse:
    """Handles data when Admin Logs In through POST requests

    Args:
        request
        **kwargs

    Returns:
        response.JsonResponse
    """
    try:
        print("ADMIN POST REQUEST LOGIN")
        print("Request Object DATA:", request.data)

        email = request.data.get("Email")
        password = request.data.get("Password")

        print(email, password)

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

    except AdminDoesNotExistError as adne:
        return response.JsonResponse(
            {"error": str(adne), "auth_status": False},
            status=status.HTTP_404_NOT_FOUND,
        )
    except InvalidAdminCredentialsError as iace:
        return response.JsonResponse(
            {"error": str(iace), "auth_status": False},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    except AdminTokenGenerationError as atge:
        return response.JsonResponse(
            {"error": str(atge), "auth_status": False},
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
        )
    except Exception as e:
        print(e)
        return response.JsonResponse(
            {
                "error": "Error Occured While Receiving Login Data",
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
        print("ADMIN GET REQUEST")

        page = int(request.query_params.get("Page"))
        record = Music_Data.fetch_data()
        # record["success_status"] = True
        # print(record)
        return Paginate.get_paginated_data(page, record)

        # return response.JsonResponse(record, status=status.HTTP_200_OK)
        # return record

    except DataFetchingError as dfe:
        return response.JsonResponse(
            {"error": str(dfe), "success_status": False},
            status=status.HTTP_404_NOT_FOUND,
        )
    except PageDoesNotExistError as pdne:
        return response.JsonResponse(
            {"error": str(pdne), "success_status": False},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Exception:
        return response.JsonResponse(
            {"error": "Error Occured While Sending Data", "success_status": False},
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
        print("ADMIN MUSIC DATA DELETE REQUEST")

        pid = request.query_params.get("PID")
        email = request.query_params.get("Email")
        print(pid, email)

        aws_s3_func = AWSFunctionsS3()
        cloud_filename = User_Data.get_cloud_filename(pid, email)
        aws_s3_func.delete_file_from_s3(cloud_filename)

        User_Data.delete_user_data(pid, email)

        return response.JsonResponse(
            {"success_status": True},
            status=status.HTTP_200_OK,
        )

    except FileDoesNotExistForCurrentUserError as fdne:
        return response.JsonResponse(
            {"error": str(fdne), "success_status": False},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Exception as e:
        return response.JsonResponse(
            {
                "error": "Error Occured While Deleting User Data",
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
        print("ADMIN POST REQUEST GET TOKENS")
        print("Request Object DATA:", request.data)

        refresh_token = request.data.get("RefreshToken")
        refresh_status = request.data.get("RefreshStatus")
        print(refresh_token, refresh_status)

        data = Admin_Token_Auth.decode_refresh_token(refresh_token)
        print(data)

        assert data["role"] == "admin"

        admin_id = data["aid"]
        print(admin_id)
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

    except InvalidTokenError as ite:
        return response.JsonResponse(
            {"error": str(ite), "success_status": False},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    except InvalidAdminIDError as iaie:
        return response.JsonResponse(
            {"error": str(iaie), "success_status": False},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Exception:
        return response.JsonResponse(
            {
                "error": "Error Occured While Receiving Refresh Token",
                "success_status": False,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
