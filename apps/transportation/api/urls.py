from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'vehicles', views.VehicleViewSet)
router.register(r'routes', views.RouteViewSet)
router.register(r'routestops', views.RouteStopViewSet)
router.register(r'transportallocations', views.TransportAllocationViewSet)
router.register(r'transportattendances', views.TransportAttendanceViewSet)
router.register(r'maintenancerecords', views.MaintenanceRecordViewSet)
router.register(r'fuelrecords', views.FuelRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
