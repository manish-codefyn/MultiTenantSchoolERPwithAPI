from rest_framework import serializers
from apps.transportation.models import *

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'

class RouteStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteStop
        fields = '__all__'

class TransportAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportAllocation
        fields = '__all__'

class TransportAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportAttendance
        fields = '__all__'

class MaintenanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRecord
        fields = '__all__'
        ref_name = "TransportationMaintenanceRecord"

class FuelRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelRecord
        fields = '__all__'

