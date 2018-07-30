from django.db import models


class User(models.Model):
    """
    User model that represents all the data we store about the buyers and sellers on Bangazon
    Author: Jacob Smith

    """
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Street = models.CharField(max_length=100)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=100)
    Zip = models.PositiveIntegerField()
    Phone = models.CharField(max_length=10)
    Email = models.CharField(max_length=50)
    Date_Created = models.DateField(auto_now_add=True)
    Last_Signon = models.DateField()
