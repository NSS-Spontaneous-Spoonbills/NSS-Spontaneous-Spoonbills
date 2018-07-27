from rest_framework.viewsets import ModelViewSet
from bangazonapi.serializers import User_Serializer
from bangazonapi.models import User

class User_View(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = User_Serializer