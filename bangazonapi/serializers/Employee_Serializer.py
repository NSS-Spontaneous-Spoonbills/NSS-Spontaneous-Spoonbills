from rest_framework import serializers
from bangazonapi.models import Employee
"""
employee serializer formats employee model to be JSON formatted.
Author: Patrick Murphy
"""

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = Employee




