from django.db import models


class Training_Program_Sessions(models.Model):
    Program_ID = models.ForeignKey(
        'Training_Program', on_delete=models.CASCADE)
    Program_Start_Date = models.DateField()
    Program_End_Date = models.DateField()
    Max_Students = models.PositiveIntegerField()
