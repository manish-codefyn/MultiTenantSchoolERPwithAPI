from rest_framework import viewsets
from apps.core.api.permissions import TenantAccessPermission, RoleRequiredPermission
from rest_framework.permissions import IsAuthenticated
from apps.core.permissions.mixins import TenantAccessMixin
from apps.students.models import *
from .serializers import *

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class GuardianViewSet(viewsets.ModelViewSet):
    queryset = Guardian.objects.all()
    serializer_class = GuardianSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class StudentAddressViewSet(viewsets.ModelViewSet):
    queryset = StudentAddress.objects.all()
    serializer_class = StudentAddressSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class StudentDocumentViewSet(viewsets.ModelViewSet):
    queryset = StudentDocument.objects.all()
    serializer_class = StudentDocumentSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class StudentMedicalInfoViewSet(viewsets.ModelViewSet):
    queryset = StudentMedicalInfo.objects.all()
    serializer_class = StudentMedicalInfoSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class StudentAcademicHistoryViewSet(viewsets.ModelViewSet):
    queryset = StudentAcademicHistory.objects.all()
    serializer_class = StudentAcademicHistorySerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class StudentIdentificationViewSet(viewsets.ModelViewSet):
    queryset = StudentIdentification.objects.all()
    serializer_class = StudentIdentificationSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

