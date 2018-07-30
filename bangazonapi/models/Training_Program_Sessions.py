from django.db import models

"""
The training program session model is an instance of the training program.
The Program_ID references the Training_Program table.
This table allows the company to run multiple instances of one program.
Author: Patrick Murphy
"""
class Training_Program_Sessions(models.Model):
    Program_ID = models.ForeignKey(
        'Training_Program', on_delete=models.CASCADE)
    Program_Start_Date = models.DateField()
    Program_End_Date = models.DateField()
    Max_Students = models.PositiveIntegerField()
