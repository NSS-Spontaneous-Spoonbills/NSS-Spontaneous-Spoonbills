from rest_framework import serializers
from bangazonapi.models import Computer

class ComputerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = Computer

