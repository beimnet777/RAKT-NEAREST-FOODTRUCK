from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FoodTruck
from .serializers import FoodTruckSerializer
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseBadRequest

class NearestFoodTrucksView(APIView):
    def get(self, request):

        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        limit = request.GET.get('limit', 10)  # Default to 10 trucks if limit not provided
        page = request.GET.get('page', 1)  # Get the page number from query params, default to 1

        try:
            limit = int(limit)
        except ValueError:
            return HttpResponseBadRequest("Limit must be an integer.")

        if latitude or longitude:  
            try:
                latitude = float(latitude)
                longitude = float(longitude)
            except:
                return HttpResponseBadRequest("Latitude and longitude must be valid numbers.")

            pipeline = [
                {
                    '$geoNear': {
                        'near': {'type': "Point", 'coordinates': [longitude, latitude]},
                        'distanceField': "distance",
                        'spherical': True
                    }
                },
                {
                    '$limit': limit
                }
            ]
            food_trucks = list(FoodTruck.objects.aggregate(*pipeline))
        else:
            # If no latitude or longitude is provided, return trucks with the given limit without distance attribute
            food_trucks = list(FoodTruck.objects.all()[:limit])
            print(food_trucks)

        #serializing query results
        serializer = FoodTruckSerializer(food_trucks, many=True)
        food_trucks = serializer.data


        # Paginate the results
        paginator = Paginator(food_trucks, 12)  # Show 12 items per page
        try:
            food_trucks_page = paginator.page(page)
        except PageNotAnInteger:
            food_trucks_page = paginator.page(1)
        except EmptyPage:
            food_trucks_page = paginator.page(paginator.num_pages)

        
        

        truck_images = [
            "https://i.ibb.co/MZMXD9r/Truck4.jpg",
            "https://i.ibb.co/bvfk7Z7/Truck3.jpg",
            "https://i.ibb.co/MZmPksy/Truck2.jpg",
            "https://i.ibb.co/WtNMK0J/Truck1.jpg", 
            "https://i.ibb.co/87V1JC8/Truck5.jpg"
        ]


        # Assign an image URL to each truck (for UI Purpose as the data doesn't contain images)
        for i, truck in enumerate(food_trucks_page):
                truck["image_url"] = truck_images[i % len(truck_images)]
        
        
        #in order to have something visibile Render has been used but we can just send json response as well
        return render(
            request,
            'nearest_food_trucks.html',
            {
                'food_trucks': food_trucks_page,
                'latitude': latitude,
                'longitude': longitude,
                'limit': limit,
                'paginator': paginator
            }
        )