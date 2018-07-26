# Register your models here.
from django.contrib import admin

from .models import User, Employee, Computer, Cust_Order, Department, Employee_Training, Employment_Dates, Ordered_Products, Payment_Options, Payment_Type, Product_Type, Product, Training_Program_Sessions, Training_Program


admin.site.register(User)
admin.site.register(Computer)
admin.site.register(Cust_Order)
admin.site.register(Department)
admin.site.register(Employee_Training)
admin.site.register(Employment_Dates)
admin.site.register(Ordered_Products)
admin.site.register(Payment_Options)
admin.site.register(Payment_Type)
admin.site.register(Product_Type)
admin.site.register(Product)
admin.site.register(Training_Program_Sessions)
admin.site.register(Training_Program)
