from rest_framework import viewsets
from bangazonapi.serializers import UserSerializer
from bangazonapi.models import User
from datetime import date


class Inactive_Customer_View(viewsets.ModelViewSet):
    """
    API endpoint that allows inactive customers to be viewed or edited.
    """
    serializer_class = UserSerializer

    def get_queryset(self):
        """Filter the queryset to show all customers who have not logged in to Bangazon in the last 6 months"""
        user_data = User.objects.all()
        inactive_users = set()
        for u in user_data:
            #  - datetime.timedelta(6*365/12)).isoformat()
            if login_date < date.today():
                inactive_users.add(u)
        queryset = inactive_users
