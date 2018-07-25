from django.db import models

class Product_Type(models.Model):
    Type_Name = models.CharField(max_length = 350)
