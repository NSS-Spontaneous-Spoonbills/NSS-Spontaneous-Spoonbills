from rest_framework import viewsets, status, mixins
from bangazonapi.serializers import Training_ProgramSerializer
from bangazonapi.models import Training_Program

class Training_Program_View(viewsets.ModelViewSet):
    """
    API endpoint that allows TrainingPrograms to be viewed or edited.
    """
    queryset = Training_Program.objects.all()
    serializer_class = Training_ProgramSerializer

    http_method_names = ['get', 'post', 'put', 'head']
