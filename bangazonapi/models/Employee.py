from django.db import models

class Employee(models.Model):
    First_Name = models.CharField(max_length = 350)
    Last_Name = models.CharField(max_length = 350)
    Dept_ID = models.ForeignKey('Department',on_delete=models.CASCADE)
    Comp_ID = models.ForeignKey('Computer',on_delete=models.CASCADE)
    Employee_Is_Active = models.BooleanField()

