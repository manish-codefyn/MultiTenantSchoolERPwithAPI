from rest_framework import viewsets
from apps.core.api.permissions import TenantAccessPermission, RoleRequiredPermission
from rest_framework.permissions import IsAuthenticated
from apps.core.permissions.mixins import TenantAccessMixin
from apps.admission.models import *
from .serializers import *

class AdmissionCycleViewSet(viewsets.ModelViewSet):
    queryset = AdmissionCycle.objects.all()
    serializer_class = AdmissionCycleSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff']

class AdmissionProgramViewSet(viewsets.ModelViewSet):
    queryset = AdmissionProgram.objects.all()
    serializer_class = AdmissionProgramSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff']

class OnlineApplicationViewSet(viewsets.ModelViewSet):
    queryset = OnlineApplication.objects.all()
    serializer_class = OnlineApplicationSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff']

class ApplicationDocumentViewSet(viewsets.ModelViewSet):
    queryset = ApplicationDocument.objects.all()
    serializer_class = ApplicationDocumentSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff']

class ApplicationGuardianViewSet(viewsets.ModelViewSet):
    queryset = ApplicationGuardian.objects.all()
    serializer_class = ApplicationGuardianSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff']

class ApplicationLogViewSet(viewsets.ModelViewSet):
    queryset = ApplicationLog.objects.all()
    serializer_class = ApplicationLogSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff']

class MeritListViewSet(viewsets.ModelViewSet):
    queryset = MeritList.objects.all()
    serializer_class = MeritListSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff']

class MeritListEntryViewSet(viewsets.ModelViewSet):
    queryset = MeritListEntry.objects.all()
    serializer_class = MeritListEntrySerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff']

class AdmissionFormConfigViewSet(viewsets.ModelViewSet):
    queryset = AdmissionFormConfig.objects.all()
    serializer_class = AdmissionFormConfigSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff']

class AdmissionStatisticsViewSet(viewsets.ModelViewSet):
    queryset = AdmissionStatistics.objects.all()
    serializer_class = AdmissionStatisticsSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'staff']

