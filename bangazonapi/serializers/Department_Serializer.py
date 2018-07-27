from rest_framework import serializers
from bangazonapi.models import Department


class Department_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = Department




