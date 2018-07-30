from django.db import models


class Cust_Order(models.Model):
    """Models data for orders a customer makes from the Bangazon website"""

    Customer_ID = models.ForeignKey('User', on_delete=models.CASCADE)
    Payment_ID = models.ForeignKey('Payment_Options', on_delete=models.CASCADE)
    Order_Date = models.DateField(auto_now_add=True)
    Ship_Date = models.DateField(blank=True)
