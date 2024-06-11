import datetime
import pdb

import requests
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RateSerializer, GetRateSerializer
from .models import Rate


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


class GetRate(APIView):
    def get(self, request):
        date = request.GET.get('date')
        curr_code = request.GET.get('curr_code')

        if not date:
            return Response({"error": "date required"}, status=status.HTTP_400_BAD_REQUEST)

        if not curr_code:
            return Response({"error": "curr_code required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            date_obj = datetime.datetime.fromisoformat(date)
        except Exception:
            return Response({"error": "invalid date format"}, status=status.HTTP_400_BAD_REQUEST)

        rate = get_object_or_404(Rate, Date=date_obj, Cur_Abbreviation=curr_code)
        data = GetRateSerializer(rate).data

        previous_day = date_obj - datetime.timedelta(days=1)
        prev_rate = Rate.objects.filter(Date=previous_day, Cur_Abbreviation=curr_code).first()

        if prev_rate:
            if prev_rate.Cur_OfficialRate > rate.Cur_OfficialRate:
                change_status = 'Decreased'
            else:
                change_status = 'Increased'
            data['Change_From_Previous_Day'] = change_status
        else:
            data['Change_From_Previous_Day'] = "No data about previous day"

        return Response(data, status=status.HTTP_200_OK)
