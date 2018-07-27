from rest_framework import viewsets
from bangazonapi.serializers import Product_Serializer
from bangazonapi.models import Product

class Product_View(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited
    """
    queryset = Product.objects.all()
    serializer_class = Product_Serializer