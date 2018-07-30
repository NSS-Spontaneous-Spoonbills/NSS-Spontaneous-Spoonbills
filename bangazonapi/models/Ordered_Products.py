from django.db import models


class Ordered_Products(models.Model):
    """Models data for every product in a given order from the Bangazon website"""
    Order_ID = models.ForeignKey('Cust_Order', on_delete=models.CASCADE)
    Product_ID = models.ForeignKey('Product', on_delete=models.CASCADE)
    Quantity = models.PositiveIntegerField()
