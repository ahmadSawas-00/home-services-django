from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet
from .views import service_list_view

router = DefaultRouter()
router.register(r'services', ServiceViewSet, basename='service')

urlpatterns = [
    path('', include(router.urls)),
    path('services-ui/', service_list_view, name='services-ui'),
]