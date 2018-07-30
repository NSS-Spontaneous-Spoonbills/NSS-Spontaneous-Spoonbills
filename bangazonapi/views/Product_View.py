from rest_framework import viewsets
from bangazonapi.serializers import ProductSerializer
from bangazonapi.models import Product

class Product_View(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited
    Author: Jacob Smith
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer