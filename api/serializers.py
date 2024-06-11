from rest_framework import serializers
from .models import Rate


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'


class GetRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = [
            'Date',
            'Cur_Abbreviation',
            'Cur_Name',
            'Cur_OfficialRate'
        ]
