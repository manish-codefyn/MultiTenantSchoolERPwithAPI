from rest_framework import serializers
from apps.students.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = '__all__'

class StudentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAddress
        fields = '__all__'

class StudentDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDocument
        fields = '__all__'

class StudentMedicalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentMedicalInfo
        fields = '__all__'

class StudentAcademicHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAcademicHistory
        fields = '__all__'

class StudentIdentificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentIdentification
        fields = '__all__'

