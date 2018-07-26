from django.db import models


class Computer(models.Model):
    Comp_Name = models.CharField(max_length=50)
    Commission_Date = models.DateField(auto_now_add=True)
    Decommission_Date = models.DateField(blank=True)
