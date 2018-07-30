from rest_framework import serializers
from bangazonapi.models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    Product serializer that takes the Product model and serializes the model to be JSON formatted and readable.

    """
    class Meta:
        fields = '__all__'
        model = Product