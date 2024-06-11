from django.urls import path

from api.views import FetchRates

urlpatterns = [
    path('fetch-rates/', FetchRates.as_view())
]
