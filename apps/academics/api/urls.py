from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'academicyears', views.AcademicYearViewSet)
router.register(r'terms', views.TermViewSet)
router.register(r'schoolclasss', views.SchoolClassViewSet)
router.register(r'sections', views.SectionViewSet)
router.register(r'houses', views.HouseViewSet)
router.register(r'housepointss', views.HousePointsViewSet)
router.register(r'subjects', views.SubjectViewSet)
router.register(r'classsubjects', views.ClassSubjectViewSet)
router.register(r'timetables', views.TimeTableViewSet)
router.register(r'studentattendances', views.StudentAttendanceViewSet)
router.register(r'holidays', views.HolidayViewSet)
router.register(r'studymaterials', views.StudyMaterialViewSet)
router.register(r'syllabuss', views.SyllabusViewSet)
router.register(r'streams', views.StreamViewSet)
router.register(r'classteachers', views.ClassTeacherViewSet)
router.register(r'gradingsystems', views.GradingSystemViewSet)
router.register(r'grades', views.GradeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
