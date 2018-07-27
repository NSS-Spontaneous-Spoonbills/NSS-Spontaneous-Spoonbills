from rest_framework import viewsets
from bangazonapi.serializers import Ordered_ProductsSerializer
from bangazonapi.models import Ordered_Products


class Ordered_Products_View(viewsets.ModelViewSet):
    """
    API endpoint that allows Ordered_Products to be viewed or edited.
    """
    queryset = Ordered_Products.objects.all()
    serializer_class = Ordered_ProductsSerializer
