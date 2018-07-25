from django.core.management.base import BaseCommand
from django_seed import Seed
seeder = Seed.seeder()
import random
from bangazonapi.models import
Training_Program,
Training_Program_Sessions,
User,
Employees,
Employment_Dates,
Department,
Computer,
Employee_Training,
Product,
Product_Type,
Cust_Order,
Ordered_Products,
Payment_Options,
Payment_Type


class Command(BaseCommand):

  def handle(self, *args, **options):
    seeder.add_entity(Training_Program, 12) # the number argument is the total num of rows you want created
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
    # seeder.add_entity(Payment_Type, 50, {'acct_number': lambda x: random.randint(11111,99999)})
    # Override the seeder "guess" of what faker provider you want it to use
    # seeder.add_entity(Product, 100, {'name': lambda x: seeder.faker.catch_phrase()})

    inserted_pks = seeder.execute()