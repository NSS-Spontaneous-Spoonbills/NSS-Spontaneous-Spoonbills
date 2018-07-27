from rest_framework import viewsets
from bangazonapi.serializers import Employment_DatesSerializer
from bangazonapi.models import Employment_Dates


class Employment_Dates_View(viewsets.ModelViewSet):
    """
    API endpoint that allows Employment_Dates to be viewed or edited.
    """
    queryset = Employment_Dates.objects.all()
    serializer_class = Employment_DatesSerializer
