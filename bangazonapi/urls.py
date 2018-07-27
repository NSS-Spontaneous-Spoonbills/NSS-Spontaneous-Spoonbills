from django.urls import path
from views import UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('user', UserViewSet, base_name='user')
urlpatterns = router.urls

