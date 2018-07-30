from django.db import models


class Payment_Options(models.Model):
    """Models data for a customer's payment accounts when making a purchase from the Bangazon website"""
    Customer_ID = models.ForeignKey('User', on_delete=models.CASCADE)
    Payment_Type_ID = models.ForeignKey(
        'Payment_Type', on_delete=models.CASCADE)
    Account_Num = models.PositiveIntegerField()
