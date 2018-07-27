from rest_framework import viewsets
from bangazonapi.serializers import Payment_TypeSerializer
from bangazonapi.models import Payment_Type

class Payment_TypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows payment types to be viewed or edited.
    """
    queryset = Payment_Type.objects.all()
    serializer_class = Payment_TypeSerializer
