from django.db import models

class Training_Program_Sessions(models.Model):
    Program_ID = models.ForeignKey('Training_Program',on_delete=models.CASCADE)
    Program_Start_Date = models.CharField(max_length = 350)
    Program_End_Date = models.CharField(max_length = 350)
    Max_Students = models.IntegerField()