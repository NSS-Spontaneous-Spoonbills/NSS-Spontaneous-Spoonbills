from django.db import models

class Payment_Options(models.Model):
    Customer_ID = models.ForeignKey('User',on_delete=models.CASCADE)
    Payment_Type_ID = models.ForeignKey('Payment_Type',on_delete=models.CASCADE)
    Account_Num = models.CharField(max_length = 350)
