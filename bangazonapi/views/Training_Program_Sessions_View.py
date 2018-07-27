from rest_framework import viewsets
from bangazonapi.serializers import Training_Program_SessionsSerializer
from bangazonapi.models import Training_Program_Sessions

class Training_Program_Sessions_View(viewsets.ModelViewSet):
    """
    API endpoint that allows training program sessions to be viewed or edited.
    """
    queryset = Training_Program_Sessions.objects.all()
    serializer_class = Training_Program_SessionsSerializer
