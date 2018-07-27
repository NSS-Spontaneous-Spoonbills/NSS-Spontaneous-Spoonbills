from rest_framework import serializers
from bangazonapi.models import Employee_Training

class Employee_TrainingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = Employee_Training