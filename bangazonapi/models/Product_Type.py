from django.db import models


class Product_Type(models.Model):
    Product_Type_Name = models.SlugField()
