from django.db import models

class Employment_Dates(models.Model):
    Employee_ID = models.ForeignKey('Employee',on_delete=models.CASCADE)
    Hire_Date = models.CharField(max_length = 350)
    Term_Date = models.CharField(max_length = 350)
