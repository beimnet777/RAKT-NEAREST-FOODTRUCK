from rest_framework import serializers
from .models import FoodTruck

class FoodTruckSerializer(serializers.Serializer):
    '''
    For this project scope only selected attributes have been included in the serializer
    '''
    _id = serializers.IntegerField()
    applicant = serializers.CharField(max_length=255)
    facility_type = serializers.CharField(max_length=100, required=False)
    address = serializers.CharField(max_length=255, required=False)
    status = serializers.CharField(max_length=100, required=False)
    food_items = serializers.CharField(required=False)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    approved = serializers.DateTimeField()
    distance = serializers.FloatField(required=False)
