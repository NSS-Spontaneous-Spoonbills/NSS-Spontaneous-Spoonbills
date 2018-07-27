from django.urls import path
from .views import User_View
from .views import Product_View
from .views import Employee_Training_View
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('user', User_View, base_name='user')
router.register('product', Product_View, base_name='product')
router.register('employee_training', Employee_Training_View, base_name='employee_training')
urlpatterns = router.urls

