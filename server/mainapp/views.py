from django.http.response import JsonResponse
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import status
from django.http import response
import requests

from .utils import recv_music_data
from mainapp import Music_Data


class Data(APIView):
    def post(self, request, **kwargs) -> JsonResponse:

        print("Receiving Data API")

        data = recv_music_data(request)

        return data

    def get(self, request, **kwargs):
        """
        Backend will be uploading data (sending)
        """
        return response.JsonResponse(data={"response": "true"})
