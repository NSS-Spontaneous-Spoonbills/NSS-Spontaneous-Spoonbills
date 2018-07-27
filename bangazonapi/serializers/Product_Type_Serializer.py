from rest_framework import serializers
from bangazonapi.models import Product_Type

class Product_TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = Product_Type
