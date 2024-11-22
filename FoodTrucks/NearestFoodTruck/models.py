from mongoengine import Document, StringField, IntField, FloatField, DateTimeField, PointField, BooleanField
from datetime import datetime
from django.utils import timezone

class FoodTruck(Document):
    _id = IntField(primary_key=True)  
    applicant = StringField()  
    facility_type = StringField()  
    cnn = IntField()  
    location_description = StringField()  
    address = StringField()  
    blocklot = StringField() 
    block = StringField()  
    lot = StringField()  
    permit = StringField()  
    status = StringField()  
    food_items = StringField()  

    # Geospatial Data
    x = FloatField()
    y = FloatField()
    latitude = FloatField()  
    longitude = FloatField()  

    location = PointField()  # Geospatial point: (latitude, longitude)

    schedule_url = StringField()  # Example: URL to schedule
    dayshours = StringField(max_length=255, null=True)    
    noisent = StringField(max_length=255, null=True)
    approved = DateTimeField(default=timezone.now)
    received = IntField(default=0)  
    
    prior_permit = BooleanField(default=False)
    expiration_date = DateTimeField(default=timezone.now)
    fire_prevention_districts = IntField(default=0)
    police_districts = IntField(default=0)
    supervisor_districts = IntField(default=0)
    zip_codes = IntField(default=0)
    neighborhoods_old = IntField(default=0) 

    meta = {
        'collection': 'food_trucks' 
    }   
