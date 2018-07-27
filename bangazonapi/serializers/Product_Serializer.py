from rest_framework import serializers
from bangazonapi.models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = Product