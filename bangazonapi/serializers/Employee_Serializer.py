from rest_framework import serializers
from bangazonapi.models import Employee


class Employee_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = Employee




