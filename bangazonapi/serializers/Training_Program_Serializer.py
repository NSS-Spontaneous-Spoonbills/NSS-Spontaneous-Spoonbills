from rest_framework import serializers
from bangazonapi.models import Training_Program

class Training_ProgramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = Training_Program




