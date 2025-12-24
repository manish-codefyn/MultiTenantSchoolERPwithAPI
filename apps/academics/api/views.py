from rest_framework import viewsets
from apps.core.api.permissions import TenantAccessPermission, RoleRequiredPermission
from rest_framework.permissions import IsAuthenticated
from apps.core.permissions.mixins import TenantAccessMixin
from apps.academics.models import *
from .serializers import *

class AcademicYearViewSet(viewsets.ModelViewSet):
    queryset = AcademicYear.objects.all()
    serializer_class = AcademicYearSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class TermViewSet(viewsets.ModelViewSet):
    queryset = Term.objects.all()
    serializer_class = TermSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class SchoolClassViewSet(viewsets.ModelViewSet):
    queryset = SchoolClass.objects.all()
    serializer_class = SchoolClassSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class HousePointsViewSet(viewsets.ModelViewSet):
    queryset = HousePoints.objects.all()
    serializer_class = HousePointsSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class ClassSubjectViewSet(viewsets.ModelViewSet):
    queryset = ClassSubject.objects.all()
    serializer_class = ClassSubjectSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class TimeTableViewSet(viewsets.ModelViewSet):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class StudentAttendanceViewSet(viewsets.ModelViewSet):
    queryset = StudentAttendance.objects.all()
    serializer_class = StudentAttendanceSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class HolidayViewSet(viewsets.ModelViewSet):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class StudyMaterialViewSet(viewsets.ModelViewSet):
    queryset = StudyMaterial.objects.all()
    serializer_class = StudyMaterialSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class SyllabusViewSet(viewsets.ModelViewSet):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class StreamViewSet(viewsets.ModelViewSet):
    queryset = Stream.objects.all()
    serializer_class = StreamSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class ClassTeacherViewSet(viewsets.ModelViewSet):
    queryset = ClassTeacher.objects.all()
    serializer_class = ClassTeacherSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class GradingSystemViewSet(viewsets.ModelViewSet):
    queryset = GradingSystem.objects.all()
    serializer_class = GradingSystemSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'parent', 'admin']

