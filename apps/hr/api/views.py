from rest_framework import viewsets
from apps.core.api.permissions import TenantAccessPermission, RoleRequiredPermission
from rest_framework.permissions import IsAuthenticated
from apps.core.permissions.mixins import TenantAccessMixin
from apps.hr.models import *
from .serializers import *

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class QualificationViewSet(viewsets.ModelViewSet):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class StaffAddressViewSet(viewsets.ModelViewSet):
    queryset = StaffAddress.objects.all()
    serializer_class = StaffAddressSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class StaffDocumentViewSet(viewsets.ModelViewSet):
    queryset = StaffDocument.objects.all()
    serializer_class = StaffDocumentSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class StaffAttendanceViewSet(viewsets.ModelViewSet):
    queryset = StaffAttendance.objects.all()
    serializer_class = StaffAttendanceSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class LeaveTypeViewSet(viewsets.ModelViewSet):
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class LeaveApplicationViewSet(viewsets.ModelViewSet):
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveApplicationSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class LeaveBalanceViewSet(viewsets.ModelViewSet):
    queryset = LeaveBalance.objects.all()
    serializer_class = LeaveBalanceSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class SalaryStructureViewSet(viewsets.ModelViewSet):
    queryset = SalaryStructure.objects.all()
    serializer_class = SalaryStructureSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class PayrollViewSet(viewsets.ModelViewSet):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class EmploymentHistoryViewSet(viewsets.ModelViewSet):
    queryset = EmploymentHistory.objects.all()
    serializer_class = EmploymentHistorySerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class TrainingProgramViewSet(viewsets.ModelViewSet):
    queryset = TrainingProgram.objects.all()
    serializer_class = TrainingProgramSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class TrainingParticipationViewSet(viewsets.ModelViewSet):
    queryset = TrainingParticipation.objects.all()
    serializer_class = TrainingParticipationSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class PerformanceReviewViewSet(viewsets.ModelViewSet):
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class RecruitmentViewSet(viewsets.ModelViewSet):
    queryset = Recruitment.objects.all()
    serializer_class = RecruitmentSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class HolidayViewSet(viewsets.ModelViewSet):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class WorkScheduleViewSet(viewsets.ModelViewSet):
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class TaxConfigViewSet(viewsets.ModelViewSet):
    queryset = TaxConfig.objects.all()
    serializer_class = TaxConfigSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class PFESIConfigViewSet(viewsets.ModelViewSet):
    queryset = PFESIConfig.objects.all()
    serializer_class = PFESIConfigSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class DisciplinaryActionViewSet(viewsets.ModelViewSet):
    queryset = DisciplinaryAction.objects.all()
    serializer_class = DisciplinaryActionSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

class AssetAssignmentViewSet(viewsets.ModelViewSet):
    queryset = AssetAssignment.objects.all()
    serializer_class = AssetAssignmentSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['hr', 'admin']

