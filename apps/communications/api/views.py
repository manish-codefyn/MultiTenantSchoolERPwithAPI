from rest_framework import status
from rest_framework.response import Response
from apps.core.api.views import (
    BaseListCreateAPIView, BaseRetrieveUpdateDestroyAPIView
)
from apps.communications.models import (
    CommunicationChannel, CommunicationTemplate, CommunicationCampaign,
    Communication, CommunicationAttachment
)
from apps.communications.api.serializers import (
    CommunicationChannelSerializer, CommunicationTemplateSerializer,
    CommunicationCampaignSerializer, CommunicationSerializer,
    CommunicationAttachmentSerializer
)

# ============================================================================
# CONFIG VIEWS
# ============================================================================

class CommunicationChannelListCreateAPIView(BaseListCreateAPIView):
    model = CommunicationChannel
    serializer_class = CommunicationChannelSerializer
    search_fields = ['name', 'code']
    filterset_fields = ['channel_type', 'is_active', 'is_healthy']
    roles_required = ['admin', 'communications_manager']

class CommunicationChannelDetailAPIView(BaseRetrieveUpdateDestroyAPIView):
    model = CommunicationChannel
    serializer_class = CommunicationChannelSerializer
    roles_required = ['admin', 'communications_manager']


class CommunicationTemplateListCreateAPIView(BaseListCreateAPIView):
    model = CommunicationTemplate
    serializer_class = CommunicationTemplateSerializer
    search_fields = ['name', 'code', 'subject']
    filterset_fields = ['channel', 'template_type', 'language', 'is_active', 'is_approved']
    roles_required = ['admin', 'communications_manager', 'teacher']

class CommunicationTemplateDetailAPIView(BaseRetrieveUpdateDestroyAPIView):
    model = CommunicationTemplate
    serializer_class = CommunicationTemplateSerializer
    roles_required = ['admin', 'communications_manager']

# ============================================================================
# CAMPAIGN VIEWS
# ============================================================================

class CommunicationCampaignListCreateAPIView(BaseListCreateAPIView):
    model = CommunicationCampaign
    serializer_class = CommunicationCampaignSerializer
    search_fields = ['name']
    filterset_fields = ['campaign_type', 'status', 'template']
    roles_required = ['admin', 'communications_manager']

class CommunicationCampaignDetailAPIView(BaseRetrieveUpdateDestroyAPIView):
    model = CommunicationCampaign
    serializer_class = CommunicationCampaignSerializer
    roles_required = ['admin', 'communications_manager']

# ============================================================================
# COMMUNICATION VIEWS
# ============================================================================

class CommunicationListCreateAPIView(BaseListCreateAPIView):
    model = Communication
    serializer_class = CommunicationSerializer
    search_fields = ['title', 'subject', 'external_recipient_email']
    filterset_fields = ['channel', 'template', 'campaign', 'status', 'direction', 'priority']
    roles_required = ['admin', 'communications_manager', 'teacher']

class CommunicationDetailAPIView(BaseRetrieveUpdateDestroyAPIView):
    model = Communication
    serializer_class = CommunicationSerializer
    roles_required = ['admin', 'communications_manager']


class CommunicationAttachmentListCreateAPIView(BaseListCreateAPIView):
    model = CommunicationAttachment
    serializer_class = CommunicationAttachmentSerializer
    search_fields = ['file_name']
    filterset_fields = ['communication', 'file_type']
    roles_required = ['admin', 'communications_manager']

class CommunicationAttachmentDetailAPIView(BaseRetrieveUpdateDestroyAPIView):
    model = CommunicationAttachment
    serializer_class = CommunicationAttachmentSerializer
    roles_required = ['admin', 'communications_manager']
