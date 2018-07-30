from rest_framework import serializers
from bangazonapi.models import Computer

class ComputerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        """employee computer serializer"""
        fields = '__all__'
        model = Computer

