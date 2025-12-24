from rest_framework import viewsets
from apps.core.api.permissions import TenantAccessPermission, RoleRequiredPermission
from rest_framework.permissions import IsAuthenticated
from apps.core.permissions.mixins import TenantAccessMixin
from apps.exams.models import *
from .serializers import *

class ExamTypeViewSet(viewsets.ModelViewSet):
    queryset = ExamType.objects.all()
    serializer_class = ExamTypeSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class ExamSubjectViewSet(viewsets.ModelViewSet):
    queryset = ExamSubject.objects.all()
    serializer_class = ExamSubjectSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class ExamResultViewSet(viewsets.ModelViewSet):
    queryset = ExamResult.objects.all()
    serializer_class = ExamResultSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class SubjectResultViewSet(viewsets.ModelViewSet):
    queryset = SubjectResult.objects.all()
    serializer_class = SubjectResultSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class MarkSheetViewSet(viewsets.ModelViewSet):
    queryset = MarkSheet.objects.all()
    serializer_class = MarkSheetSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class CompartmentExamViewSet(viewsets.ModelViewSet):
    queryset = CompartmentExam.objects.all()
    serializer_class = CompartmentExamSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class ResultStatisticsViewSet(viewsets.ModelViewSet):
    queryset = ResultStatistics.objects.all()
    serializer_class = ResultStatisticsSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

