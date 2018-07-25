from django.db import models

class Employee_Training(models.Model):
    Session_ID = models.ForeignKey('Training_Program',on_delete=models.CASCADE)
    Employee_ID = models.ForeignKey('Employee',on_delete=models.CASCADE)
    Completed = models.BooleanField()