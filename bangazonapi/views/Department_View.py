from rest_framework.viewsets import ModelViewSet
from bangazonapi.serializers import Department_Serializer
from bangazonapi.models import Department

class Department_View(ModelViewSet):
    """
    API endpoint that allows Departments to be viewed or edited.
    """
    queryset = Department.objects.all()
    serializer_class = Department_Serializer





#     from rest_framework.viewsets import ModelViewSet
# from developers.models import Developers
# from .serializers import DevSerializer


# class DevViewSet(ModelViewSet):
#     queryset = Developers.objects.all()
#     serializer_class = DevSerializer