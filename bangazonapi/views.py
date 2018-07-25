from django.contrib.auth.models import User
from rest_framework import viewsets
from bangazonapi.models.User import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited"""
    queryset = User.objects.all().order_by('User_ID')
    serializer_class = UserSerializer