"""
This file is responsible for handling all the routing for each of our pages through Rest Framework : DefaultRouter
"""
from django.urls import path
from .views import User_View
from .views import Product_View
from .views import Employee_Training_View
from .views import Cust_OrderViewSet
from .views import Employment_DatesViewSet
from .views import Ordered_ProductsViewSet
from .views import Payment_OptionsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('user', User_View, base_name='user')
router.register('product', Product_View, base_name='product')
router.register('employee_training', Employee_Training_View, base_name='employee_training')
router.register('cust_order', Cust_OrderViewSet, base_name='cust_order')
router.register('employment_dates', Employment_DatesViewSet,base_name='employment_dates')
router.register('ordered_products', Ordered_ProductsViewSet, base_name='ordered_products')
router.register('payment_options', Payment_OptionsViewSet, base_name='payment_options')
urlpatterns = router.urls
