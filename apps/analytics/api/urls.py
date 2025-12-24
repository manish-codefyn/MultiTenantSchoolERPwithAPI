from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'auditanalysisreports', views.AuditAnalysisReportViewSet)
router.register(r'auditpatterns', views.AuditPatternViewSet)
router.register(r'auditalerts', views.AuditAlertViewSet)
router.register(r'auditdashboards', views.AuditDashboardViewSet)
router.register(r'auditmetrics', views.AuditMetricViewSet)
router.register(r'auditmetricvalues', views.AuditMetricValueViewSet)
router.register(r'datasources', views.DataSourceViewSet)
router.register(r'kpimodels', views.KPIModelViewSet)
router.register(r'kpivalues', views.KPIValueViewSet)
router.register(r'reports', views.ReportViewSet)
router.register(r'reportexecutions', views.ReportExecutionViewSet)
router.register(r'dashboards', views.DashboardViewSet)
router.register(r'dashboardwidgets', views.DashboardWidgetViewSet)
router.register(r'predictivemodels', views.PredictiveModelViewSet)
router.register(r'studentperformanceanalyticss', views.StudentPerformanceAnalyticsViewSet)
router.register(r'institutionalanalyticss', views.InstitutionalAnalyticsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
