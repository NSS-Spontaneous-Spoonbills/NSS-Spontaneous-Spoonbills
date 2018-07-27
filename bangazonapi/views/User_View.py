from rest_framework import viewsets
from bangazonapi.serializers import UserSerializer
from bangazonapi.models import User

class User_View(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer