from rest_framework import serializers
from apps.core.models import *

class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = '__all__'
        ref_name = "CoreAuditLog"

