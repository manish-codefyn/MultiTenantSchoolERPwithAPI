from rest_framework import serializers
from apps.hostel.models import *

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = '__all__'

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'

class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class HostelAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostelAllocation
        fields = '__all__'

class HostelAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostelAttendance
        fields = '__all__'

class LeaveApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveApplication
        fields = '__all__'
        ref_name = "HostelLeaveApplication"

class MessMenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MessMenuCategory
        fields = '__all__'

class MessMenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessMenuItem
        fields = '__all__'

class DailyMessMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyMessMenu
        fields = '__all__'

class DailyMenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyMenuItem
        fields = '__all__'

class HostelMessSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostelMessSubscription
        fields = '__all__'

class MessAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessAttendance
        fields = '__all__'

class MessFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessFeedback
        fields = '__all__'

