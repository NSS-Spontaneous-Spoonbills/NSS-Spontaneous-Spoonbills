from rest_framework import serializers
from bangazonapi.models import Employee_Training

class Employee_TrainingSerializer(serializers.HyperlinkedModelSerializer):
    """
        Employee Training serializer that takes the Employee Training model and serializes the model to be JSON formatted and readable.
        Author: Jacob Smith

    """
    class Meta:
        fields = '__all__'
        model = Employee_Training