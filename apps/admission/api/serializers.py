from rest_framework import serializers
from apps.admission.models import *

class AdmissionCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionCycle
        fields = '__all__'

class AdmissionProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionProgram
        fields = '__all__'

class OnlineApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineApplication
        fields = '__all__'

class ApplicationDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationDocument
        fields = '__all__'

class ApplicationGuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationGuardian
        fields = '__all__'

class ApplicationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationLog
        fields = '__all__'

class MeritListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeritList
        fields = '__all__'

class MeritListEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MeritListEntry
        fields = '__all__'

class AdmissionFormConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionFormConfig
        fields = '__all__'

class AdmissionStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionStatistics
        fields = '__all__'

