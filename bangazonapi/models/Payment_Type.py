from django.db import models


class Payment_Type(models.Model):
    """models for customer payment types"""
    Payment_Type_Name = models.SlugField()
