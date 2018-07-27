from django.urls import path
from views import UserViewSet
from views import ComputerViewSet
from views import Payment_TypeViewSet
from views import Product_TypeViewSet
from views import Training_Program_SessionsViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('user', UserViewSet, base_name='user')
router.register('computer', ComputerViewSet, base_name='computer')
router.register('product_type', Product_TypeViewSet, base_name='product_type')
router.register('payment_type', Payment_TypeViewSet, base_name='payment_type')
router.register('training_program_sessions', Training_Program_SessionsViewSet, base_name='training_program_sessions')
urlpatterns = router.urls

