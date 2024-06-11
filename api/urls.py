from django.urls import path

from api.views import FetchRates, GetRate

urlpatterns = [
    path('fetch-rates/', FetchRates.as_view()),
    path('get-rate/', GetRate.as_view())
]
