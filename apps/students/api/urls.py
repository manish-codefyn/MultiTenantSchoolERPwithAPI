from django.urls import path
from .views import (
    # Main Student Views
    StudentListAPIView,
    StudentCreateAPIView,
    StudentDetailAPIView,
    StudentUpdateAPIView,
    StudentDeleteAPIView,
    StudentRetrieveUpdateDestroyAPIView,
    
    # Action Views
    StudentIDCardAPIView,
    StudentPromoteAPIView,
    StudentReportCardAPIView,
    
    # Bulk & Data Views
    StudentBulkActionAPIView,
    StudentBulkCreateAPIView,
    StudentExportAPIView,
    StudentImportAPIView,
    
    # Search & Stats Views
    StudentSearchAPIView,
    StudentAutocompleteAPIView,
    StudentStatisticsAPIView,
    StudentDashboardAPIView,
    
    # Related Model Views
    StudentGuardianListCreateAPIView,
    StudentGuardianDetailAPIView,
    StudentAddressListCreateAPIView,
    StudentAddressDetailAPIView,
    StudentDocumentListCreateAPIView,
    StudentDocumentDetailAPIView,
    StudentDocumentVerifyAPIView,
    StudentDocumentRejectAPIView
)
from .dashboard_view import StudentStatsDashboardAPIView

urlpatterns = [
    # ==================================================================
    # MAIN STUDENT ENDPOINTS
    # ==================================================================
    
    # Dashboard (Aggregate)
    path('dashboard/', StudentStatsDashboardAPIView.as_view(), name='dashboard-aggregate'),
    
    # List and Create
    path('', StudentListAPIView.as_view(), name='student-list'),
    path('create/', StudentCreateAPIView.as_view(), name='student-create'),
    
    # Advanced Search & Autocomplete
    path('search/', StudentSearchAPIView.as_view(), name='student-search'),
    path('autocomplete/', StudentAutocompleteAPIView.as_view(), name='student-autocomplete'),
    
    # Statistics & Dashboard
    path('statistics/', StudentStatisticsAPIView.as_view(), name='student-statistics'),
    path('dashboard/<uuid:pk>/', StudentDashboardAPIView.as_view(), name='student-dashboard'),
    
    # Import/Export
    path('export/', StudentExportAPIView.as_view(), name='student-export'),
    path('import/', StudentImportAPIView.as_view(), name='student-import'),
    path('bulk/create/', StudentBulkCreateAPIView.as_view(), name='student-bulk-create'),
    path('bulk/actions/', StudentBulkActionAPIView.as_view(), name='student-bulk-actions'),
    
    # Detail Operations (Retrieve, Update, Delete)
    # Put this after specific paths like search/ export/ etc to avoid conflict
    path('<uuid:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name='student-detail'),
    path('<uuid:pk>/update/', StudentUpdateAPIView.as_view(), name='student-update'),
    path('<uuid:pk>/delete/', StudentDeleteAPIView.as_view(), name='student-delete'),
    
    # ==================================================================
    # STUDENT ACTION ENDPOINTS
    # ==================================================================
    
    path('<uuid:pk>/id-card/', StudentIDCardAPIView.as_view(), name='student-id-card'),
    path('<uuid:pk>/promote/', StudentPromoteAPIView.as_view(), name='student-promote'),
    path('<uuid:pk>/report-card/', StudentReportCardAPIView.as_view(), name='student-report-card'),
    
    # ==================================================================
    # RELATED MODEL ENDPOINTS (NESTED & DIRECT)
    # ==================================================================
    
    # Guardians
    path('<uuid:student_id>/guardians/', StudentGuardianListCreateAPIView.as_view(), name='student-guardian-list'),
    path('guardians/<uuid:pk>/', StudentGuardianDetailAPIView.as_view(), name='student-guardian-detail'),
    
    # Addresses
    path('<uuid:student_id>/addresses/', StudentAddressListCreateAPIView.as_view(), name='student-address-list'),
    path('addresses/<uuid:pk>/', StudentAddressDetailAPIView.as_view(), name='student-address-detail'),
    
    # Documents
    path('<uuid:student_id>/documents/', StudentDocumentListCreateAPIView.as_view(), name='student-document-list'),
    path('documents/<uuid:pk>/', StudentDocumentDetailAPIView.as_view(), name='student-document-detail'),
    # Document Actions (using nested routing on the viewset logic or explicit paths)
    # Since we are using BaseRetrieveUpdateDestroyAPIView which doesn't auto-route @action unless using a Router,
    # we might need to manually map these extra actions if they are defined as @action on a ViewSet.
    # However, here they are defined as @action on a generic APIView subclass? 
    # Wait, @action decorator only works with ViewSets.
    # The views in views.py are inheriting from BaseRetrieveUpdateDestroyAPIView which mimics generic views.
    # If StudentDocumentDetailAPIView uses @action, it MUST be a ViewSet or we manually map URLs.
    # Checking StudentDocumentDetailAPIView... it has @action methods `verify` and `reject`.
    # But it inherits from BaseRetrieveUpdateDestroyAPIView.
    # If BaseRetrieveUpdateDestroyAPIView is a GenericAPIView, @action won't work automatically.
    # We should map them manually.
    
    path('documents/<uuid:pk>/verify/', StudentDocumentVerifyAPIView.as_view(), name='student-document-verify'),
    path('documents/<uuid:pk>/reject/', StudentDocumentRejectAPIView.as_view(), name='student-document-reject'),
]
