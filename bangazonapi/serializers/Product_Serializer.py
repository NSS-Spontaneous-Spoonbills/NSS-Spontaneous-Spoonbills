from rest_framework import serializers
from bangazonapi.models import Product

class Product_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = Product