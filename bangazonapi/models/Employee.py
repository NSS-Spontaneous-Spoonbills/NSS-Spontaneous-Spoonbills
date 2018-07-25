from django.db import models

class Employee(models.Model):
    First_Name = models.CharField()
    Last_Name = models.CharField()
    Dept_ID = models.ForeignKey('Department',on_delete=models.CASCADE)
    Comp_ID = models.ForeignKey('Computer',on_delete=models.CASCADE)
    Employee_Is_Active = models.BooleanField()

    # FOREIGN KEY (Dept_ID) REFERENCES Department (Department_ID),
    # FOREIGN KEY (Comp_ID) REFERENCES Computer (Comp_ID)