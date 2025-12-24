from rest_framework import serializers
from apps.exams.models import *

class ExamTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamType
        fields = '__all__'

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class ExamSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamSubject
        fields = '__all__'

class ExamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = '__all__'

class SubjectResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectResult
        fields = '__all__'

class MarkSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkSheet
        fields = '__all__'

class CompartmentExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompartmentExam
        fields = '__all__'

class ResultStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultStatistics
        fields = '__all__'

