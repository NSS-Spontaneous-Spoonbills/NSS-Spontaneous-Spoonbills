from django.db import models


class Product_Type(models.Model):
    """models for types of products"""
    Product_Type_Name = models.SlugField()
