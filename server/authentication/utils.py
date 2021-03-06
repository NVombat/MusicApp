from rest_framework import status
from django.http import response

from .errors import (
    InvalidUserCredentialsError,
    InvalidVerificationError,
    UserDoesNotExistError,
    TokenGenerationError,
    InvalidTokenError,
    UserExistsError,
    InvalidUIDError,
)
from .mailer import send_reset_pwd_mail
from . import Token_Auth, User_Auth


def register_user(request, **kwargs) -> response.JsonResponse:
    """Handles data when user registers through POST requests

    Args:
        request
        **kwargs

    Returns:
        response.JsonResponse
    """
    try:
        email = request.data.get("Email")
        password = request.data.get("Password")

        User_Auth.insert_user(email, password)
        uid = User_Auth.get_uid(email)
        payload = {"id": uid}

        token = Token_Auth.generate_token(
            payload=payload, expiry=1, get_refresh=True, refresh_exipry=48
        )

        return response.JsonResponse(
            data={
                "access_token": token["access_token"],
                "refresh_token": token["refresh_token"],
            },
            status=status.HTTP_201_CREATED,
        )

    except UserExistsError:
        return response.JsonResponse(
            {"error_status": True, "auth_status": False},
            status=status.HTTP_400_BAD_REQUEST,
        )
    except UserDoesNotExistError:
        return response.JsonResponse(
            {"error_status": True, "auth_status": False},
            status=status.HTTP_404_NOT_FOUND,
        )
    except TokenGenerationError:
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


def login_user(request, **kwargs) -> response.JsonResponse:
    """Handles data when user Logs In through POST requests

    Args:
        request
        **kwargs

    Returns:
        response.JsonResponse
    """
    try:
        email = request.data.get("Email")
        password = request.data.get("Password")

        if User_Auth.check_hash(email, password):
            uid = User_Auth.get_uid(email)
            payload = {"id": uid}

            token = Token_Auth.generate_token(
                payload=payload, expiry=1, get_refresh=True, refresh_exipry=48
            )

            return response.JsonResponse(
                data={
                    "access_token": token["access_token"],
                    "refresh_token": token["refresh_token"],
                },
                status=status.HTTP_200_OK,
            )

    except UserDoesNotExistError:
        return response.JsonResponse(
            {"error_status": True, "auth_status": False},
            status=status.HTTP_404_NOT_FOUND,
        )
    except InvalidUserCredentialsError:
        return response.JsonResponse(
            {"error_status": True, "auth_status": False},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    except TokenGenerationError:
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


def reset_pwd(request, **kwargs) -> response.JsonResponse:
    """Handles data when user resets password through POST requests

    Args:
        request
        **kwargs

    Returns:
        response.JsonResponse
    """
    try:
        email = request.data.get("Email")
        user_id = User_Auth.get_uid(email)

        base_url = "https://www.vr1music.com"
        reset_url = base_url + "?reset=True&uid=" + user_id
        send_reset_pwd_mail(email, reset_url)

        return response.JsonResponse(
            data={"success_status": True},
            status=status.HTTP_200_OK,
        )

    except UserDoesNotExistError:
        return response.JsonResponse(
            {"error_status": True, "auth_status": False},
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


def reset_pwd_data(request, **kwargs) -> response.JsonResponse:
    """Handles data when user resets password through POST request ON THE LINK

    Args:
        request
        **kwargs

    Returns:
        response.JsonResponse
    """
    try:
        pwd = request.data.get("Password")
        verif_code = request.data.get("Code")

        if User_Auth.check_verif_code(verif_code):
            hashed_pwd = User_Auth.hash_password(pwd)
            User_Auth.reset_password(hashed_pwd, verif_code)

        return response.JsonResponse(
            data={"success_status": True},
            status=status.HTTP_200_OK,
        )

    except InvalidVerificationError:
        return response.JsonResponse(
            {"error_status": True, "success_status": False},
            status=status.HTTP_401_UNAUTHORIZED,
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
    """Verifies refresh token and generates new tokens

    Args:
        request
        **kwargs

    Returns:
        response.JsonResponse
    """
    try:
        refresh_token = request.data.get("RefreshToken")
        refresh_status = request.data.get("RefreshStatus")

        data = Token_Auth.decode_refresh_token(refresh_token)

        assert data["role"] == "user"

        user_id = data["id"]

        if User_Auth.validate_uid(user_id):
            payload = {"id": user_id}

            if refresh_status == "True":
                acc_token = Token_Auth.generate_token(
                    payload=payload, expiry=1, get_refresh=False
                )

                return response.JsonResponse(
                    data={
                        "access_token": acc_token,
                    },
                    status=status.HTTP_200_OK,
                )

            elif refresh_status == "False":
                token = Token_Auth.generate_token(
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
    except InvalidUIDError:
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
