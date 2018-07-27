from rest_framework import serializers
from bangazonapi.models import Payment_Options


class Payment_OptionsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        fields = ('id', 'Customer_ID', 'Payment_Type_ID', 'Account_Num')
        model = Payment_Options
