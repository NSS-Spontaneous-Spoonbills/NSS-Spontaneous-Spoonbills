from rest_framework import serializers
from bangazonapi.models import User

class User_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = User




