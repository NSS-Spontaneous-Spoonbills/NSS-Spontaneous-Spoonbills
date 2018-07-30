from django.db import models

"""
Model that includes name and description of training program.
Author: Patrick Murphy
"""
class Training_Program(models.Model):
    Program_Name = models.SlugField()
    Program_Description = models.CharField(max_length=350)
