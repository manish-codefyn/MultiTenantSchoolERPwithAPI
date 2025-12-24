from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)
router.register(r'qualifications', views.QualificationViewSet)
router.register(r'designations', views.DesignationViewSet)
router.register(r'staffs', views.StaffViewSet)
router.register(r'staffaddresss', views.StaffAddressViewSet)
router.register(r'staffdocuments', views.StaffDocumentViewSet)
router.register(r'staffattendances', views.StaffAttendanceViewSet)
router.register(r'leavetypes', views.LeaveTypeViewSet)
router.register(r'leaveapplications', views.LeaveApplicationViewSet)
router.register(r'leavebalances', views.LeaveBalanceViewSet)
router.register(r'salarystructures', views.SalaryStructureViewSet)
router.register(r'payrolls', views.PayrollViewSet)
router.register(r'promotions', views.PromotionViewSet)
router.register(r'employmenthistorys', views.EmploymentHistoryViewSet)
router.register(r'trainingprograms', views.TrainingProgramViewSet)
router.register(r'trainingparticipations', views.TrainingParticipationViewSet)
router.register(r'performancereviews', views.PerformanceReviewViewSet)
router.register(r'recruitments', views.RecruitmentViewSet)
router.register(r'jobapplications', views.JobApplicationViewSet)
router.register(r'holidays', views.HolidayViewSet)
router.register(r'workschedules', views.WorkScheduleViewSet)
router.register(r'taxconfigs', views.TaxConfigViewSet)
router.register(r'pfesiconfigs', views.PFESIConfigViewSet)
router.register(r'disciplinaryactions', views.DisciplinaryActionViewSet)
router.register(r'assets', views.AssetViewSet)
router.register(r'assetassignments', views.AssetAssignmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
