import pdb

import requests
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RateSerializer


class FetchRates(APIView):
    def post(self, request):
        date = self.request.data.get('date')
        url = f"https://api.nbrb.by/exrates/rates?ondate={date}&periodicity=0"
        response = requests.get(url)
        if response.status_code == 200:
            response_data = response.json()
            serializer = RateSerializer(data=response_data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=response.status_code)

