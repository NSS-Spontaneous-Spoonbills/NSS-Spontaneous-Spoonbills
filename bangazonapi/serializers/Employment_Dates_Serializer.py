from rest_framework import serializers
from bangazonapi.models import Employment_Dates


class Employment_DatesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        fields = ('id', 'Employee_ID', 'Hire_Date', 'Term_Date')
        model = Employment_Dates
