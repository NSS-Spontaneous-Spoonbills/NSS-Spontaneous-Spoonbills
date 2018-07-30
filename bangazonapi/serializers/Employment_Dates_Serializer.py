from rest_framework import serializers
from bangazonapi.models import Employment_Dates


class Employment_DatesSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes data from the Employment_Dates model"""
    class Meta:
        fields = ('id', 'Employee_ID', 'Hire_Date', 'Term_Date')
        model = Employment_Dates
