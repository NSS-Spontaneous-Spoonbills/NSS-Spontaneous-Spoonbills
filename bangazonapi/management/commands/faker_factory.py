from django.core.management.base import BaseCommand
from django_seed import Seed
seeder = Seed.seeder()
import random
from bangazonapi.models import


class Command(BaseCommand):

    def handle(self, *args, **options):
        # the number argument is the total num of rows you want created
        seeder.add_entity(Training_Program, 12)
        seeder.add_entity(Training_Program_Sessions, 12)
        seeder.add_entity(User, 12)
        seeder.add_entity(Employees, 12)
        seeder.add_entity(Employment_Dates, 12)
        seeder.add_entity(Department, 12)
        seeder.add_entity(Computer, 12)
        seeder.add_entity(Employee_Training, 12)
        seeder.add_entity(Product, 25)
        seeder.add_entity(Product_Type, 12)
        seeder.add_entity(Cust_Order, 12)
        seeder.add_entity(Ordered_Products, 12)
        seeder.add_entity(Payment_Options, 12)
        seeder.add_entity(Payment_Type, 12)

        inserted_pks = seeder.execute()
