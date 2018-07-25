from django.db import models

class Computer(models.Model):
    Comp_Name =  models.CharField(max_length = 350)
    Commission_Date = models.CharField(max_length = 350)
    Decommission_Date = models.CharField(max_length = 350)