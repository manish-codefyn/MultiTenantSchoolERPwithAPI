from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'amenitys', views.AmenityViewSet)
router.register(r'facilitys', views.FacilityViewSet)
router.register(r'hostels', views.HostelViewSet)
router.register(r'rooms', views.RoomViewSet)
router.register(r'hostelallocations', views.HostelAllocationViewSet)
router.register(r'hostelattendances', views.HostelAttendanceViewSet)
router.register(r'leaveapplications', views.LeaveApplicationViewSet)
router.register(r'messmenucategorys', views.MessMenuCategoryViewSet)
router.register(r'messmenuitems', views.MessMenuItemViewSet)
router.register(r'dailymessmenus', views.DailyMessMenuViewSet)
router.register(r'dailymenuitems', views.DailyMenuItemViewSet)
router.register(r'hostelmesssubscriptions', views.HostelMessSubscriptionViewSet)
router.register(r'messattendances', views.MessAttendanceViewSet)
router.register(r'messfeedbacks', views.MessFeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
