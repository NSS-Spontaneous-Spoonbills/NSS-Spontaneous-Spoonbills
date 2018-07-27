from rest_framework import viewsets
from bangazonapi.serializers import Payment_OptionsSerializer
from bangazonapi.models import Payment_Options


class Payment_Options_View(viewsets.ModelViewSet):
    """
    API endpoint that allows Payment_Options to be viewed or edited.
    """
    queryset = Payment_Options.objects.all()
    serializer_class = Payment_OptionsSerializer
