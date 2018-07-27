from rest_framework import viewsets
from bangazonapi.serializers import EmployeeSerializer
from bangazonapi.models import Employee

class Employee_View(viewsets.ModelViewSet):
    """
    API endpoint that allows Employees to be viewed or edited.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    http_method_names = ['get', 'put', 'post', 'head']