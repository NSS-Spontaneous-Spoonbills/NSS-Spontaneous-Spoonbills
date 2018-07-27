from django.urls import path
from views import UserViewSet
from views import Computer_View
from views import Payment_Type_View
from views import Product_Type_View
from views import Training_Program_Sessions_View
from views import Cust_OrderViewSet
from views import Employment_DatesViewSet
from views import Ordered_ProductsViewSet
from views import Payment_OptionsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', UserViewSet, base_name='user')
router.register('computer', Computer_View, base_name='computer')
router.register('product_type', Product_Type_View, base_name='product_type')
router.register('payment_type', Payment_Type_View, base_name='payment_type')
router.register('training_program_sessions', Training_Program_Sessions_View, base_name='training_program_sessions')
router.register('cust_order', Cust_OrderViewSet, base_name='cust_order')
router.register('employment_dates', Employment_DatesViewSet,
                base_name='employment_dates')
router.register('ordered_products', Ordered_ProductsViewSet,
                base_name='ordered_products')
router.register('payment_options', Payment_OptionsViewSet,
                base_name='payment_options')
urlpatterns = router.urls
