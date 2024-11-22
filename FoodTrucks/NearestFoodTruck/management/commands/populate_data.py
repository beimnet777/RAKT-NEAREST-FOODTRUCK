import csv
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime
from NearestFoodTruck.models import FoodTruck

class Command(BaseCommand):
    '''
    Populate mongodb with data from CSV file as stated in the project description.
    '''
    help = 'Populate datas from a CSV file into MongoDB.'

    def add_arguments(self, parser):
        parser.add_argument('csv_filename', type=str, help='CSV file name to import the data from.')

    def handle(self, *args, **kwargs):
        csv_filename = kwargs['csv_filename']  

        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                try:
                    food_truck = FoodTruck(
                        _id=int(row['locationid']),
                        applicant=row['Applicant'],
                        facility_type=row['FacilityType'],
                        cnn=int(row['cnn']) if row['cnn'] else None,
                        location_description=row['LocationDescription'],
                        address=row['Address'],
                        blocklot=row['blocklot'],
                        block=row['block'],
                        lot=row['lot'],
                        permit=row['permit'],
                        status=row['Status'],
                        food_items=row['FoodItems'],
                        x=float(row['X']) if row['X'] else None,
                        y=float(row['Y']) if row['Y'] else None,
                        latitude=float(row['Latitude']) if row['Latitude'] else None,
                        longitude=float(row['Longitude']) if row['Longitude'] else None,
                        schedule_url=row['Schedule'],
                        dayshours=row['dayshours'],
                        noisent=row['NOISent'],
                        approved=parse_datetime(row['Approved']),
                        received=int(row['Received']) if row['Received'] else None,
                        prior_permit=bool(row['PriorPermit']),
                        expiration_date=parse_datetime(row['ExpirationDate']),
                        fire_prevention_districts=int(row['Fire Prevention Districts']),
                        police_districts=int(row['Police Districts']),
                        supervisor_districts=int(row['Supervisor Districts']),
                        zip_codes=int(row['Zip Codes']),
                        neighborhoods_old=int(row['Neighborhoods (old)']),
                        location={'type': 'Point', 'coordinates': [float(row['Longitude']),  float(row['Latitude'])]} if row['Longitude'] and row['Latitude'] else None,
                    )
                    food_truck.save()
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error importing row: {e}'))

            self.stdout.write(self.style.SUCCESS('Successfully imported food trucks data from {}.'.format(csv_filename)))