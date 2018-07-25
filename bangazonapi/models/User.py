from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('User_ID', 'First_Name','Last_Name', 'Street', 'City', 'State', 'Zip', 'Phone', 'Email', 'Date_Created', 'Last_Signon')