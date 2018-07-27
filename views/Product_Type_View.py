from rest_framework import viewsets
from bangazonapi.serializers import Product_TypeSerializer
from bangazonapi.models import Product_Type

class Product_TypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product types to be viewed or edited.
    """
    queryset = Product_Type.objects.all()
    serializer_class = Product_TypeSerializer
