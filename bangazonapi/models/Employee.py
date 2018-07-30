from django.db import models
"""
Employee model that represents data on employees.  Has foreign keys of Department and Computer.
Author: Patrick Murphy
"""

class Employee(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Dept_ID = models.ForeignKey('Department', on_delete=models.CASCADE)
    Comp_ID = models.ForeignKey('Computer', on_delete=models.CASCADE)
    Is_Supervisor = models.BooleanField(default=False)
    Employee_Is_Active = models.BooleanField(default=True)
