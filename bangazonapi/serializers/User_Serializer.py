from rest_framework import serializers
from bangazonapi.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    User serializer that takes the User model and serializes the model to be JSON formatted and readable.
    Author: Jacob Smith

    """
    class Meta:
        fields = '__all__'
        model = User




