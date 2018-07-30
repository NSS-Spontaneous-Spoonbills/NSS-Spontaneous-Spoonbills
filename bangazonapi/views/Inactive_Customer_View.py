from rest_framework import viewsets
from bangazonapi.serializers import Inactive_UserSerializer
from bangazonapi.models import User
import datetime


class Inactive_Customer_View(viewsets.ModelViewSet):
    """
    API endpoint that allows inactive customers to be viewed or edited.
    """
    serializer_class = Inactive_UserSerializer

    def get_queryset(self):
        """Filter the queryset to show all customers who have not logged in to Bangazon in the last 6 months"""
        user_data = User.objects.all()
        inactive_users = set()
        for u in user_data:
            if u.Last_Signon < (datetime.date.today() + datetime.timedelta(days=-340)):

                inactive_users.add(u)
        queryset = inactive_users
        return queryset
