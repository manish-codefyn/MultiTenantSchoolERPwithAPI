from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'examtypes', views.ExamTypeViewSet)
router.register(r'exams', views.ExamViewSet)
router.register(r'examsubjects', views.ExamSubjectViewSet)
router.register(r'examresults', views.ExamResultViewSet)
router.register(r'subjectresults', views.SubjectResultViewSet)
router.register(r'marksheets', views.MarkSheetViewSet)
router.register(r'compartmentexams', views.CompartmentExamViewSet)
router.register(r'resultstatisticss', views.ResultStatisticsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
