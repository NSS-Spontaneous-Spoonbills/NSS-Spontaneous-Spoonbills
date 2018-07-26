from django.db import models

class Department(models.Model):
    Dept_Name = models.CharField(max_length = 350)
    Supervisor_ID = models.ForeignKey('Employee',on_delete=models.CASCADE)
    Remaining_Budget = models.IntegerField()

