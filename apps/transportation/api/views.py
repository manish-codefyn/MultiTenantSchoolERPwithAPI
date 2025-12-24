from rest_framework import viewsets
from apps.core.api.permissions import TenantAccessPermission, RoleRequiredPermission
from rest_framework.permissions import IsAuthenticated
from apps.core.permissions.mixins import TenantAccessMixin
from apps.transportation.models import *
from .serializers import *

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff', 'parent']

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff', 'parent']

class RouteStopViewSet(viewsets.ModelViewSet):
    queryset = RouteStop.objects.all()
    serializer_class = RouteStopSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff', 'parent']

class TransportAllocationViewSet(viewsets.ModelViewSet):
    queryset = TransportAllocation.objects.all()
    serializer_class = TransportAllocationSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff', 'parent']

class TransportAttendanceViewSet(viewsets.ModelViewSet):
    queryset = TransportAttendance.objects.all()
    serializer_class = TransportAttendanceSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff', 'parent']

class MaintenanceRecordViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRecord.objects.all()
    serializer_class = MaintenanceRecordSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff', 'parent']

class FuelRecordViewSet(viewsets.ModelViewSet):
    queryset = FuelRecord.objects.all()
    serializer_class = FuelRecordSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff', 'parent']

