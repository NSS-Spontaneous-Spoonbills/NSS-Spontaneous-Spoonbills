from rest_framework import serializers
from bangazonapi.models import Ordered_Products


class Ordered_ProductsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        fields = ('id', 'Order_ID', 'Product_ID', 'Quantity')
        model = Ordered_Products
