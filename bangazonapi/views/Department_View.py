from rest_framework import viewsets
from bangazonapi.serializers import DepartmentSerializer
from bangazonapi.models import Department

class Department_View(viewsets.ModelViewSet):
    """
    API endpoint that allows Departments to be viewed or edited.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    http_method_names = ['get', 'post', 'put', 'head']
    