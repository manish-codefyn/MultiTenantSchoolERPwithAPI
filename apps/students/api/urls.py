from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'guardians', views.GuardianViewSet)
router.register(r'studentaddresss', views.StudentAddressViewSet)
router.register(r'studentdocuments', views.StudentDocumentViewSet)
router.register(r'studentmedicalinfos', views.StudentMedicalInfoViewSet)
router.register(r'studentacademichistorys', views.StudentAcademicHistoryViewSet)
router.register(r'studentidentifications', views.StudentIdentificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
