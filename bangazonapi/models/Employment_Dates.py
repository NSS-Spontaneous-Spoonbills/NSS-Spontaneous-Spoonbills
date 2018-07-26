from django.db import models


class Employment_Dates(models.Model):
    Employee_ID = models.ForeignKey('Employee', on_delete=models.CASCADE)
    Hire_Date = models.DateField(auto_now_add=True)
    Term_Date = models.DateField(blank=True)
