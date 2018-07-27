"""
This file is responsible for handling all the routing for each of our pages through Rest Framework : DefaultRouter
"""
from django.urls import path
from .views import User_View
from .views import Product_View
from .views import Employee_Training_View
from .views import Cust_Order_View
from .views import Employment_Dates_View
from .views import Ordered_Products_View
from .views import Payment_Options_View
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('user', User_View, base_name='user')
router.register('product', Product_View, base_name='product')
router.register('employee_training', Employee_Training_View, base_name='employee_training')
router.register('cust_order', Cust_Order_View, base_name='cust_order')
router.register('employment_dates', Employment_Dates_View,base_name='employment_dates')
router.register('ordered_products', Ordered_Products_View, base_name='ordered_products')
router.register('payment_options', Payment_Options_View, base_name='payment_options')
urlpatterns = router.urls
