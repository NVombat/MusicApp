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
        print("POST REQUEST REGISTER")
        print("Request Object DATA:", request.data)

        name = request.data.get("Name")
        email = request.data.get("Email")
        password = request.data.get("Password")

        print(name, email, password)

        User_Auth.insert_user(name, email, password)
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

    except UserExistsError as uee:
        return response.JsonResponse(
            {"error": str(uee), "auth_status": False},
            status=status.HTTP_400_BAD_REQUEST,
        )
    except UserDoesNotExistError as udne:
        return response.JsonResponse(
            {"error": str(udne), "auth_status": False},
            status=status.HTTP_404_NOT_FOUND,
        )
    except TokenGenerationError as tge:
        return response.JsonResponse(
            {"error": str(tge), "auth_status": False},
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
        )
    except Exception as e:
        print(e)
        return response.JsonResponse(
            {
                "error": "Error Occured While Receiving Registration Data",
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
        print("POST REQUEST LOGIN")
        print("Request Object DATA:", request.data)

        email = request.data.get("Email")
        password = request.data.get("Password")

        print(email, password)

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

    except UserDoesNotExistError as udne:
        return response.JsonResponse(
            {"error": str(udne), "auth_status": False},
            status=status.HTTP_404_NOT_FOUND,
        )
    except InvalidUserCredentialsError as ice:
        return response.JsonResponse(
            {"error": str(ice), "auth_status": False},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    except TokenGenerationError as tge:
        return response.JsonResponse(
            {"error": str(tge), "auth_status": False},
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


def reset_pwd(request, **kwargs) -> response.JsonResponse:
    """Handles data when user resets password through POST requests

    Args:
        request
        **kwargs

    Returns:
        response.JsonResponse
    """
    try:
        print("POST REQUEST RESET PASSWORD")
        print("Request Object DATA:", request.data)

        email = request.data.get("Email")
        user_id = User_Auth.get_uid(email)

        base_url = "https://www.vr1music.com"
        reset_url = base_url + "?reset=True&uid=" + user_id
        send_reset_pwd_mail(email, reset_url)

        return response.JsonResponse(
            data={"success_status": True},
            status=status.HTTP_200_OK,
        )

    except UserDoesNotExistError as udne:
        return response.JsonResponse(
            {"error": str(udne), "auth_status": False},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Exception as e:
        print(e)
        return response.JsonResponse(
            {
                "error": "Error Occured While Receiving Reset Password Data",
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
        print("POST REQUEST RESET PASSWORD LINK")
        print("Request Object DATA:", request.data)

        pwd = request.data.get("Password")
        verif_code = request.data.get("Code")

        if User_Auth.check_verif_code(verif_code):
            hashed_pwd = User_Auth.hash_password(pwd)
            User_Auth.reset_password(hashed_pwd, verif_code)

        return response.JsonResponse(
            data={"success_status": True},
            status=status.HTTP_200_OK,
        )

    except InvalidVerificationError as ive:
        return response.JsonResponse(
            {"error": str(ive), "success_status": False},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    except Exception as e:
        print(e)
        return response.JsonResponse(
            {
                "error": "Error Occured While Receiving Reset Password Data From Link",
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
        print("POST REQUEST GET TOKENS")
        print("Request Object DATA:", request.data)

        refresh_token = request.data.get("RefreshToken")
        refresh_status = request.data.get("RefreshStatus")
        print(refresh_token, refresh_status)

        data = Token_Auth.decode_refresh_token(refresh_token)
        print(data)

        user_id = data["id"]
        print(user_id)
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

    except InvalidTokenError as ite:
        return response.JsonResponse(
            {"error": str(ite), "success_status": False},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    except InvalidUIDError as iue:
        return response.JsonResponse(
            {"error": str(iue), "success_status": False},
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
