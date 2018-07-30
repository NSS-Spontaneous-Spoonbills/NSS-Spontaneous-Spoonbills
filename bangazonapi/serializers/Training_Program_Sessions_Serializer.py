from rest_framework import serializers
from bangazonapi.models import Training_Program_Sessions

class Training_Program_SessionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        """ serializer for employee training program sessions"""
        fields = '__all__'
        model = Training_Program_Sessions
