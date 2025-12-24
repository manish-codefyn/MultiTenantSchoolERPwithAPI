from rest_framework import viewsets
from apps.core.api.permissions import TenantAccessPermission, RoleRequiredPermission
from rest_framework.permissions import IsAuthenticated
from apps.core.permissions.mixins import TenantAccessMixin
from apps.hostel.models import *
from .serializers import *

class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff', 'student']

class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff', 'student']

class HostelViewSet(viewsets.ModelViewSet):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff', 'student']

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff', 'student']

class HostelAllocationViewSet(viewsets.ModelViewSet):
    queryset = HostelAllocation.objects.all()
    serializer_class = HostelAllocationSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff', 'student']

class HostelAttendanceViewSet(viewsets.ModelViewSet):
    queryset = HostelAttendance.objects.all()
    serializer_class = HostelAttendanceSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff', 'student']

class LeaveApplicationViewSet(viewsets.ModelViewSet):
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveApplicationSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff', 'student']

class MessMenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MessMenuCategory.objects.all()
    serializer_class = MessMenuCategorySerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff', 'student']

class MessMenuItemViewSet(viewsets.ModelViewSet):
    queryset = MessMenuItem.objects.all()
    serializer_class = MessMenuItemSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff', 'student']

class DailyMessMenuViewSet(viewsets.ModelViewSet):
    queryset = DailyMessMenu.objects.all()
    serializer_class = DailyMessMenuSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff', 'student']

class DailyMenuItemViewSet(viewsets.ModelViewSet):
    queryset = DailyMenuItem.objects.all()
    serializer_class = DailyMenuItemSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff', 'student']

class HostelMessSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = HostelMessSubscription.objects.all()
    serializer_class = HostelMessSubscriptionSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff', 'student']

class MessAttendanceViewSet(viewsets.ModelViewSet):
    queryset = MessAttendance.objects.all()
    serializer_class = MessAttendanceSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff', 'student']

class MessFeedbackViewSet(viewsets.ModelViewSet):
    queryset = MessFeedback.objects.all()
    serializer_class = MessFeedbackSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff', 'student']

