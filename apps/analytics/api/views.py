from rest_framework import viewsets
from apps.core.api.permissions import TenantAccessPermission, RoleRequiredPermission
from rest_framework.permissions import IsAuthenticated
from apps.core.permissions.mixins import TenantAccessMixin
from apps.analytics.models import *
from .serializers import *

class AuditAnalysisReportViewSet(viewsets.ModelViewSet):
    queryset = AuditAnalysisReport.objects.all()
    serializer_class = AuditAnalysisReportSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'super_admin']

class AuditPatternViewSet(viewsets.ModelViewSet):
    queryset = AuditPattern.objects.all()
    serializer_class = AuditPatternSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'super_admin']

class AuditAlertViewSet(viewsets.ModelViewSet):
    queryset = AuditAlert.objects.all()
    serializer_class = AuditAlertSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'super_admin']

class AuditDashboardViewSet(viewsets.ModelViewSet):
    queryset = AuditDashboard.objects.all()
    serializer_class = AuditDashboardSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'super_admin']

class AuditMetricViewSet(viewsets.ModelViewSet):
    queryset = AuditMetric.objects.all()
    serializer_class = AuditMetricSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'super_admin']

class AuditMetricValueViewSet(viewsets.ModelViewSet):
    queryset = AuditMetricValue.objects.all()
    serializer_class = AuditMetricValueSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'super_admin']

class DataSourceViewSet(viewsets.ModelViewSet):
    queryset = DataSource.objects.all()
    serializer_class = DataSourceSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'super_admin']

class KPIModelViewSet(viewsets.ModelViewSet):
    queryset = KPIModel.objects.all()
    serializer_class = KPIModelSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'super_admin']

class KPIValueViewSet(viewsets.ModelViewSet):
    queryset = KPIValue.objects.all()
    serializer_class = KPIValueSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'super_admin']

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'super_admin']

class ReportExecutionViewSet(viewsets.ModelViewSet):
    queryset = ReportExecution.objects.all()
    serializer_class = ReportExecutionSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'super_admin']

class DashboardViewSet(viewsets.ModelViewSet):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'super_admin']

class DashboardWidgetViewSet(viewsets.ModelViewSet):
    queryset = DashboardWidget.objects.all()
    serializer_class = DashboardWidgetSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'super_admin']

class PredictiveModelViewSet(viewsets.ModelViewSet):
    queryset = PredictiveModel.objects.all()
    serializer_class = PredictiveModelSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'super_admin']

class StudentPerformanceAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = StudentPerformanceAnalytics.objects.all()
    serializer_class = StudentPerformanceAnalyticsSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'super_admin']

class InstitutionalAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = InstitutionalAnalytics.objects.all()
    serializer_class = InstitutionalAnalyticsSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['admin', 'super_admin']

