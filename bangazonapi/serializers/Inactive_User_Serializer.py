from rest_framework import serializers
from bangazonapi.models import User


class Inactive_UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = User
