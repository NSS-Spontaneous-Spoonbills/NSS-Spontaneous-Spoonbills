from rest_framework import viewsets
from bangazonapi.serializers import Cust_OrderSerializer
from bangazonapi.models import Cust_Order


class Cust_Order_View(viewsets.ModelViewSet):
    """
    API endpoint that allows Cust_Orders to be viewed or edited.
    """
    queryset = Cust_Order.objects.all()
    serializer_class = Cust_OrderSerializer
