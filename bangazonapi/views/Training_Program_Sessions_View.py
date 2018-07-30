from rest_framework import viewsets
from bangazonapi.serializers import Training_Program_SessionsSerializer
from bangazonapi.models import Training_Program_Sessions

from rest_framework import status
from rest_framework.response import Response
import datetime

class Training_Program_Sessions_View(viewsets.ModelViewSet):
    """
    API endpoint that allows training program sessions to be viewed or edited.
    """
    queryset = Training_Program_Sessions.objects.all()
    serializer_class = Training_Program_SessionsSerializer

    def destroy(self, request, *args, **kwargs):
        """
        Overrides delete method built into Django.
        All Training program sessions have delete button,
        but if program is in the past, hitting delete button will do nothing.
        If program is in future, instance will be deleted.
        Author: Patrick Murphy
        """
        instance = self.get_object()
        instance_time = instance.Program_Start_Date
        now = datetime.datetime.now().date()
        if now < instance_time:
            self.perform_destroy(instance)
        else:
            Response(status=status.HTTP_403_FORBIDDEN)

