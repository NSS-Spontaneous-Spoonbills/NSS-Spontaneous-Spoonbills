from django.db import models

class Training_Program(models.Model):
    Program_Name = models.CharField(max_length = 350)
    Program_Description = models.CharField(max_length = 350)