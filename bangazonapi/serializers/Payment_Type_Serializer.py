from rest_framework import serializers
from bangazonapi.models import Payment_Type

class Payment_TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        """ payment type serializer """
        fields = '__all__'
        model = Payment_Type
