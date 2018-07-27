from .User_View import UserViewSet
from .Computer_View import Computer_View
from .Product_Type_View import Product_Type_View
from .Payment_Type_View import Payment_Type_View
from .Training_Program_Sessions_View import Training_Program_Sessions_View
from .Cust_Order_View import Cust_OrderViewSet
from .Employment_Dates_View import Employment_DatesViewSet
from .Ordered_Products_View import Ordered_ProductsViewSet
from .Payment_Options_View import Payment_OptionsViewSet

from django.contrib.auth.models import User
from rest_framework import viewsets
