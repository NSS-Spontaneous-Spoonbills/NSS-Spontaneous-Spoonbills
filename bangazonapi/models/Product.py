from django.db import models


class Product(models.Model):
    Type_ID = models.ForeignKey('Product_Type', on_delete=models.CASCADE)
    Seller_ID = models.ForeignKey('User', on_delete=models.CASCADE)
    Title = models.CharField(max_length=350)
    Price = models.PositiveIntegerField()
    Description = models.CharField(max_length=350)
    Quantity = models.PositiveIntegerField()
