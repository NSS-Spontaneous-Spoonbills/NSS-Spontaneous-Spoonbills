from django.core.management.base import BaseCommand
from django_seed import Seed
seeder = Seed.seeder()
import random
from bangazonapi.models import Employee
from bangazonapi.models import Computer
from bangazonapi.models import Department
from bangazonapi.models import User
from bangazonapi.models import Employee_Training
from bangazonapi.models import Ordered_Products
from bangazonapi.models import Payment_Options
from bangazonapi.models import Payment_Type
from bangazonapi.models import Product_Type
from bangazonapi.models import Product
from bangazonapi.models import Training_Program_Sessions
from bangazonapi.models import Training_Program
from bangazonapi.models import Cust_Order
from bangazonapi.models import Employment_Dates


class Command(BaseCommand):
    """Allows command line integration for faker_factory.py"""

    def handle(self, *args, **options):
        """Utilizes Faker to create mock data for the database, The arguments for most seeds are ([Model], [Number of records])."""

        # the number argument is the total num of rows you want created

        seeder.add_entity(Training_Program, 12)
        seeder.add_entity(Training_Program_Sessions, 12)
        seeder.add_entity(User, 12)
        seeder.add_entity(Department, 12)
        seeder.add_entity(Computer, 12)
        seeder.add_entity(Employee, 12)
        seeder.add_entity(Employment_Dates, 12)
        seeder.add_entity(Employee_Training, 12)
        seeder.add_entity(Product_Type, 12)
        seeder.add_entity(
            Product, 25, {'Title': lambda x: seeder.faker.catch_phrase()})
        seeder.add_entity(Payment_Type, 12)
        seeder.add_entity(Payment_Options, 12, {
                          'Account_Num': lambda x: random.randint(11111, 99999)})

        seeder.add_entity(Cust_Order, 12)
        seeder.add_entity(Ordered_Products, 12)

        inserted_pks = seeder.execute()
