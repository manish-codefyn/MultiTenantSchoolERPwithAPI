from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'rolepermissions', views.RolePermissionViewSet)
router.register(r'apitokens', views.APITokenViewSet)
router.register(r'securityevents', views.SecurityEventViewSet)
router.register(r'loginattempts', views.LoginAttemptViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
