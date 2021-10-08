from django.http.response import JsonResponse
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import status
from django.http import response
import requests

from .utils import recv_music_data, send_music_data
from mainapp import Music_Data


class Data(APIView):
    def post(self, request, **kwargs) -> JsonResponse:
        """
        When User Uploads -> Data is received via POST request
        """

        print("Receiving Data API")

        data = recv_music_data(request)

        return data

    def get(self, request, **kwargs) -> JsonResponse:
        """
        When User Requests Data -> Data is sent via JsonResponse
        """

        print("Sending Data API")

        data = send_music_data(request)

        return data
