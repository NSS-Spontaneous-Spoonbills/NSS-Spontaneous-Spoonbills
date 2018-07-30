from rest_framework import serializers
from bangazonapi.models import Cust_Order


class Cust_OrderSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes data from the Cust_Orders model"""

    class Meta:
        fields = ('id', 'Customer_ID', 'Payment_ID', 'Order_Date', 'Ship_Date')
        model = Cust_Order
