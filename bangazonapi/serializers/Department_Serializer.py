from rest_framework import serializers
from bangazonapi.models import Department


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = Department




