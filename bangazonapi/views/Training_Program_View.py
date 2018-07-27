from rest_framework import viewsets, status, mixins
from bangazonapi.serializers import Training_ProgramSerializer
from bangazonapi.models import Training_Program

from rest_framework.response import Response
from django.http import Http404
import datetime


class Training_Program_View(viewsets.ModelViewSet):
    """
    API endpoint that allows TrainingPrograms to be viewed or edited.
    """
    queryset = Training_Program.objects.all()
    serializer_class = Training_ProgramSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance_time = instance.start_date
            now = datetime.datetime.now().date()
            if now < instance_time:
                self.perform_destroy(instance)
            else:
                Response(content, status=status.HTTP_403_FORBIDDEN)

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)