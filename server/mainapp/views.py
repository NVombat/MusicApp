from django.http.response import JsonResponse
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import status
from django.http import response

from mainapp import Music_Data


class UserLogin(APIView):
    def post(self, request, **kwargs) -> JsonResponse:
        """
        Backend receiving data (downloading)
        """
        return response.JsonResponse(data="TestPOST", status=status.HTTP_200_OK)

    def get(self, request, **kwargs):
        """
        Backend will be uploading data (sending)
        """
        return response.JsonResponse(data="TestGET")
