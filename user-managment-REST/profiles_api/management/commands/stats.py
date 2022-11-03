import csv, os
from profiles_api.models import UserProfile
from django.core.management.base import BaseCommand

class Command(BaseCommand):  
    def handle(self, *args, **kwargs):  
        with open("data.csv", 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                try:
                    _, created = UserProfile.objects.get_or_create(
                        id=row[0],
                        name=row[1],
                        )
                except:
                    pass
                    #sentry trace
        return "Success"

