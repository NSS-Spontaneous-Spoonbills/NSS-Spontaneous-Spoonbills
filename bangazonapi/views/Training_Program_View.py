from rest_framework import viewsets
from bangazonapi.serializers import Training_Program_Serializer
from bangazonapi.models import Training_Program

class Training_Program_View(viewsets.ModelViewSet):
    """
    API endpoint that allows TrainingPrograms to be viewed or edited.
    """
    queryset = Training_Program.objects.all()
    serializer_class = Training_Program_Serializer