from rest_framework import serializers
from bangazonapi.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ('id', 'First_Name', 'Last_Name', 'Street', 'City', 'Zip', 'Phone', 'Email', 'Date_Created', 'Last_Signon')
        model = User




