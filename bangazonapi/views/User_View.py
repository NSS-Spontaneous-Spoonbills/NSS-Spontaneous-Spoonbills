from rest_framework import viewsets
from bangazonapi.serializers import User_Serializer
from bangazonapi.models import User

class User_View(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = User_Serializer