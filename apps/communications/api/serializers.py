from rest_framework import serializers
from apps.communications.models import *

class CommunicationChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationChannel
        fields = '__all__'

class CommunicationTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationTemplate
        fields = '__all__'

class CommunicationCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationCampaign
        fields = '__all__'

class CommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication
        fields = '__all__'

class CommunicationAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationAttachment
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class MessageThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageThread
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class MessageRecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageRecipient
        fields = '__all__'

class SystemMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemMessage
        fields = '__all__'

class CommunicationPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationPreference
        fields = '__all__'

class CommunicationAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationAnalytics
        fields = '__all__'

