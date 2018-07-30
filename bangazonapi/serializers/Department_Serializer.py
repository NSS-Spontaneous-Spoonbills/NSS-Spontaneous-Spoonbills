from rest_framework import serializers
from bangazonapi.models import Department
"""
department serializer formats department model to be JSON formatted.
Author: Patrick Murphy
"""

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = Department




