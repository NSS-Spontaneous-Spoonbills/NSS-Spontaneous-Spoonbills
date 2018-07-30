from rest_framework import serializers
from bangazonapi.models import Training_Program

"""
Training_Program serializer formats Training_Program model to be JSON formatted.
Author: Patrick Murphy
"""
class Training_ProgramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = Training_Program




