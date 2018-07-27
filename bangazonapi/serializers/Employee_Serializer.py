from rest_framework import serializers
from bangazonapi.models import Employee


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = Employee




