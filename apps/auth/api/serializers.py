from rest_framework import serializers
from apps.auth.models import *

class RolePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePermission
        fields = '__all__'

class APITokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIToken
        fields = '__all__'

class SecurityEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityEvent
        fields = '__all__'

class LoginAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginAttempt
        fields = '__all__'

