from rest_framework import viewsets
from apps.core.api.permissions import TenantAccessPermission, RoleRequiredPermission
from rest_framework.permissions import IsAuthenticated
from apps.core.permissions.mixins import TenantAccessMixin
from apps.auth.models import *
from .serializers import *

class RolePermissionViewSet(viewsets.ModelViewSet):
    queryset = RolePermission.objects.all()
    serializer_class = RolePermissionSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

class APITokenViewSet(viewsets.ModelViewSet):
    queryset = APIToken.objects.all()
    serializer_class = APITokenSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

class SecurityEventViewSet(viewsets.ModelViewSet):
    queryset = SecurityEvent.objects.all()
    serializer_class = SecurityEventSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

class LoginAttemptViewSet(viewsets.ModelViewSet):
    queryset = LoginAttempt.objects.all()
    serializer_class = LoginAttemptSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

