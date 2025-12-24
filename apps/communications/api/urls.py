from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'communicationchannels', views.CommunicationChannelViewSet)
router.register(r'communicationtemplates', views.CommunicationTemplateViewSet)
router.register(r'communicationcampaigns', views.CommunicationCampaignViewSet)
router.register(r'communications', views.CommunicationViewSet)
router.register(r'communicationattachments', views.CommunicationAttachmentViewSet)
router.register(r'notifications', views.NotificationViewSet)
router.register(r'messagethreads', views.MessageThreadViewSet)
router.register(r'messages', views.MessageViewSet)
router.register(r'messagerecipients', views.MessageRecipientViewSet)
router.register(r'systemmessages', views.SystemMessageViewSet)
router.register(r'communicationpreferences', views.CommunicationPreferenceViewSet)
router.register(r'communicationanalyticss', views.CommunicationAnalyticsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
