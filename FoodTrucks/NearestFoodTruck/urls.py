# urls.py
from django.urls import path
from .views import NearestFoodTrucksView

urlpatterns = [
    path('foodtrucksnearby/', NearestFoodTrucksView.as_view(), name='food_trucks_nearby'),
]
