from django.db import models


class Employee_Training(models.Model):
    """
    Employee Training model that represents and stores the training program id, employee who attended the training, and whether the program was completed.
    Author: Jacob Smith

    """
    Session_ID = models.ForeignKey(
        'Training_Program_Sessions', on_delete=models.CASCADE)
    Employee_ID = models.ForeignKey('Employee', on_delete=models.CASCADE)
    Completed = models.BooleanField(default=False)
