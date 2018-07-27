from rest_framework import viewsets
from bangazonapi.serializers import Employee_TrainingSerializer
from bangazonapi.models import Employee_Training

class Employee_Training_View(viewsets.ModelViewSet):
    """
    API endpoint that allows employee training to be viewed or edited.
    """
    queryset = Employee_Training.objects.all()
    serializer_class = Employee_TrainingSerializer