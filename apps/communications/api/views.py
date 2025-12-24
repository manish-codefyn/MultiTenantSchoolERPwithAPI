from rest_framework import viewsets
from apps.core.api.permissions import TenantAccessPermission, RoleRequiredPermission
from rest_framework.permissions import IsAuthenticated
from apps.core.permissions.mixins import TenantAccessMixin
from apps.communications.models import *
from .serializers import *

class CommunicationChannelViewSet(viewsets.ModelViewSet):
    queryset = CommunicationChannel.objects.all()
    serializer_class = CommunicationChannelSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

class CommunicationTemplateViewSet(viewsets.ModelViewSet):
    queryset = CommunicationTemplate.objects.all()
    serializer_class = CommunicationTemplateSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

class CommunicationCampaignViewSet(viewsets.ModelViewSet):
    queryset = CommunicationCampaign.objects.all()
    serializer_class = CommunicationCampaignSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

class CommunicationViewSet(viewsets.ModelViewSet):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

class CommunicationAttachmentViewSet(viewsets.ModelViewSet):
    queryset = CommunicationAttachment.objects.all()
    serializer_class = CommunicationAttachmentSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

class MessageThreadViewSet(viewsets.ModelViewSet):
    queryset = MessageThread.objects.all()
    serializer_class = MessageThreadSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

class MessageRecipientViewSet(viewsets.ModelViewSet):
    queryset = MessageRecipient.objects.all()
    serializer_class = MessageRecipientSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

class SystemMessageViewSet(viewsets.ModelViewSet):
    queryset = SystemMessage.objects.all()
    serializer_class = SystemMessageSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

class CommunicationPreferenceViewSet(viewsets.ModelViewSet):
    queryset = CommunicationPreference.objects.all()
    serializer_class = CommunicationPreferenceSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

class CommunicationAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = CommunicationAnalytics.objects.all()
    serializer_class = CommunicationAnalyticsSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

