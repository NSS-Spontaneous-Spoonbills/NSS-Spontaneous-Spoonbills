from django.db import models
"""
Model representing Department.
Author: Patrick Murphy
"""

class Department(models.Model):
    Dept_Name = models.SlugField()
    Remaining_Budget = models.IntegerField()
