from rest_framework import serializers
from apps.analytics.models import *

class AuditAnalysisReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditAnalysisReport
        fields = '__all__'

class AuditPatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditPattern
        fields = '__all__'

class AuditAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditAlert
        fields = '__all__'

class AuditDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditDashboard
        fields = '__all__'

class AuditMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditMetric
        fields = '__all__'

class AuditMetricValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditMetricValue
        fields = '__all__'

class DataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSource
        fields = '__all__'

class KPIModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = KPIModel
        fields = '__all__'

class KPIValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = KPIValue
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class ReportExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportExecution
        fields = '__all__'

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = '__all__'

class DashboardWidgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashboardWidget
        fields = '__all__'

class PredictiveModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictiveModel
        fields = '__all__'

class StudentPerformanceAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPerformanceAnalytics
        fields = '__all__'

class InstitutionalAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutionalAnalytics
        fields = '__all__'

