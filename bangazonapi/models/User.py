from django.db import models

class User(models.Model):
    First_Name = models.CharField(max_length = 350)
    Last_Name = models.CharField(max_length = 350)
    Street = models.CharField(max_length = 350)
    City = models.CharField(max_length = 350)
    State = models.CharField(max_length = 350)
    Zip = models.IntegerField()
    Phone = models.CharField(max_length = 350)
    Email = models.CharField(max_length = 350)
    Date_Created = models.CharField(max_length = 350)
    Last_Signon = models.CharField(max_length = 350)