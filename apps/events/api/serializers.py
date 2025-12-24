from rest_framework import serializers
from apps.events.models import *

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegistration
        fields = '__all__'

class EventDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDocument
        fields = '__all__'

class EventTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventTask
        fields = '__all__'

class EventExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventExpense
        fields = '__all__'

class EventGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventGallery
        fields = '__all__'

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = '__all__'

class EventFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventFeedback
        fields = '__all__'

class RecurringEventPatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecurringEventPattern
        fields = '__all__'

