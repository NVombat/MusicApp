from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.http import response


def music_data_api(request, **kwargs):
    try:
        if request.GET[""]:
            pass

        else:
            pass

        return response.JsonResponse(data="Test", status=status.HTTP_200_OK)

    except Exception as e:
        return response.JsonResponse(
            {"error": "Error Occured"}, status=status.HTTP_400_BAD_REQUEST
        )
