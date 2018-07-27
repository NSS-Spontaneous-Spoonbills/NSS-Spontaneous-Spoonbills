from rest_framework import viewsets
from bangazonapi.serializers import DepartmentSerializer
from bangazonapi.models import Department

class Department_View(viewsets.ModelViewSet):
    """
    API endpoint that allows Departments to be viewed or edited.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer





#     from rest_framework.viewsets import ModelViewSet
# from developers.models import Developers
# from .serializers import DevSerializer


# class DevViewSet(ModelViewSet):
#     queryset = Developers.objects.all()
#     serializer_class = DevSerializer