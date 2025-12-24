from rest_framework import viewsets
from apps.core.api.permissions import TenantAccessPermission, RoleRequiredPermission
from rest_framework.permissions import IsAuthenticated
from apps.core.permissions.mixins import TenantAccessMixin
from apps.events.models import *
from .serializers import *

class EventCategoryViewSet(viewsets.ModelViewSet):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

class EventRegistrationViewSet(viewsets.ModelViewSet):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

class EventDocumentViewSet(viewsets.ModelViewSet):
    queryset = EventDocument.objects.all()
    serializer_class = EventDocumentSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

class EventTaskViewSet(viewsets.ModelViewSet):
    queryset = EventTask.objects.all()
    serializer_class = EventTaskSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

class EventExpenseViewSet(viewsets.ModelViewSet):
    queryset = EventExpense.objects.all()
    serializer_class = EventExpenseSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

class EventGalleryViewSet(viewsets.ModelViewSet):
    queryset = EventGallery.objects.all()
    serializer_class = EventGallerySerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

class EventFeedbackViewSet(viewsets.ModelViewSet):
    queryset = EventFeedback.objects.all()
    serializer_class = EventFeedbackSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

class RecurringEventPatternViewSet(viewsets.ModelViewSet):
    queryset = RecurringEventPattern.objects.all()
    serializer_class = RecurringEventPatternSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]

