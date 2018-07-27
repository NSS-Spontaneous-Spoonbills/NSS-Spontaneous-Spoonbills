from rest_framework import viewsets
from bangazonapi.serializers import ComputerSerializer
from bangazonapi.models import Computer

class Computer_View(viewsets.ModelViewSet):
    """
    API endpoint that allows computers to be viewed or edited.
    """
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
