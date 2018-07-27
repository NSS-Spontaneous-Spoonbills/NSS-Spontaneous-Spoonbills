from django.db import models


class Payment_Type(models.Model):
    Payment_Type_Name = models.SlugField()
