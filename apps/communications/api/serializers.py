from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.core.api.serializers import TenantAwareSerializer, RelatedFieldAlternative
from apps.communications.models import (
    CommunicationChannel, CommunicationTemplate, CommunicationCampaign,
    Communication, CommunicationAttachment
)

User = get_user_model()

# ============================================================================
# HELPER SERIALIZERS
# ============================================================================

class SimpleUserSerializer(serializers.ModelSerializer):
    """Simple serializer for user details"""
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'role']

# ============================================================================
# CONFIG SERIALIZERS
# ============================================================================

class CommunicationChannelSerializer(TenantAwareSerializer):
    class Meta:
        model = CommunicationChannel
        fields = '__all__'

class CommunicationTemplateSerializer(TenantAwareSerializer):
    channel_detail = RelatedFieldAlternative(
        source='channel',
        read_only=True,
        serializer=CommunicationChannelSerializer
    )
    approved_by_detail = RelatedFieldAlternative(
        source='approved_by',
        read_only=True,
        serializer=SimpleUserSerializer
    )
    
    # Computed
    available_variables = serializers.ListField(source='get_available_variables', read_only=True)

    class Meta:
        model = CommunicationTemplate
        fields = '__all__'
        read_only_fields = ['id', 'available_variables']

# ============================================================================
# CAMPAIGN SERIALIZERS
# ============================================================================

class CommunicationCampaignSerializer(TenantAwareSerializer):
    template_detail = RelatedFieldAlternative(
        source='template',
        read_only=True,
        serializer=CommunicationTemplateSerializer
    )
    
    # Computed
    delivery_rate = serializers.FloatField(read_only=True)
    open_rate = serializers.FloatField(read_only=True)
    click_rate = serializers.FloatField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = CommunicationCampaign
        fields = '__all__'
        read_only_fields = ['id', 'delivery_rate', 'open_rate', 'click_rate', 'is_active']

# ============================================================================
# COMMUNICATION SERIALIZERS
# ============================================================================

class CommunicationSerializer(TenantAwareSerializer):
    channel_detail = RelatedFieldAlternative(
        source='channel',
        read_only=True,
        serializer=CommunicationChannelSerializer
    )
    template_detail = RelatedFieldAlternative(
        source='template',
        read_only=True,
        serializer=CommunicationTemplateSerializer
    )
    campaign_detail = RelatedFieldAlternative(
        source='campaign',
        read_only=True,
        serializer=CommunicationCampaignSerializer
    )
    sender_detail = RelatedFieldAlternative(
        source='sender',
        read_only=True,
        serializer=SimpleUserSerializer
    )

    # Computed
    recipient_name = serializers.CharField(read_only=True)
    recipient_contact = serializers.CharField(read_only=True)
    is_scheduled = serializers.BooleanField(read_only=True)
    can_retry = serializers.BooleanField(read_only=True)

    class Meta:
        model = Communication
        fields = '__all__'
        read_only_fields = ['id', 'recipient_name', 'recipient_contact', 'is_scheduled', 'can_retry']

class CommunicationAttachmentSerializer(TenantAwareSerializer):
    communication_detail = RelatedFieldAlternative(
        source='communication',
        read_only=True,
        serializer=CommunicationSerializer
    )

    class Meta:
        model = CommunicationAttachment
        fields = '__all__'
