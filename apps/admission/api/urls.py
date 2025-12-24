from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'admissioncycles', views.AdmissionCycleViewSet)
router.register(r'admissionprograms', views.AdmissionProgramViewSet)
router.register(r'onlineapplications', views.OnlineApplicationViewSet)
router.register(r'applicationdocuments', views.ApplicationDocumentViewSet)
router.register(r'applicationguardians', views.ApplicationGuardianViewSet)
router.register(r'applicationlogs', views.ApplicationLogViewSet)
router.register(r'meritlists', views.MeritListViewSet)
router.register(r'meritlistentrys', views.MeritListEntryViewSet)
router.register(r'admissionformconfigs', views.AdmissionFormConfigViewSet)
router.register(r'admissionstatisticss', views.AdmissionStatisticsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
