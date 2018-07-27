from django.db import models


class Department(models.Model):
    Dept_Name = models.SlugField()
    Remaining_Budget = models.IntegerField()
