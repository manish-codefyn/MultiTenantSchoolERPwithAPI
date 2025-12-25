from django.urls import path
from apps.attendance.api.views import (
    StudentAttendanceListCreateAPIView, StudentAttendanceDetailAPIView,
    StaffAttendanceListCreateAPIView, StaffAttendanceDetailAPIView,
    HostelAttendanceListCreateAPIView, HostelAttendanceDetailAPIView,
    TransportAttendanceListCreateAPIView, TransportAttendanceDetailAPIView,
    MarkQRAttendanceAPIView, StudentListByClassAPIView, BulkAttendanceUpdateAPIView,
    MarkFaceAttendanceAPIView, AttendanceStatsAPIView, AttendanceHistoryListAPIView, 
    AttendanceExportAPIView
)

urlpatterns = [
    # QR & Face Marking
    path('mark-qr/', MarkQRAttendanceAPIView.as_view(), name='api-mark-qr'),
    path('mark-face/', MarkFaceAttendanceAPIView.as_view(), name='api-mark-face'),
    
    # Bulk & Manual
    path('students-by-class/', StudentListByClassAPIView.as_view(), name='api-students-by-class'),
    path('bulk-update/', BulkAttendanceUpdateAPIView.as_view(), name='api-bulk-update'),
    
    # Dashboard & Reports
    path('stats/', AttendanceStatsAPIView.as_view(), name='api-attendance-stats'),
    path('history/', AttendanceHistoryListAPIView.as_view(), name='api-attendance-history'),
    path('export/', AttendanceExportAPIView.as_view(), name='api-attendance-export'),

    # Student Attendance
    path('student/', StudentAttendanceListCreateAPIView.as_view(), name='studentattendance-list'),
    path('student/<uuid:pk>/', StudentAttendanceDetailAPIView.as_view(), name='studentattendance-detail'),

    # Staff Attendance
    path('staff/', StaffAttendanceListCreateAPIView.as_view(), name='staffattendance-list'),
    path('staff/<uuid:pk>/', StaffAttendanceDetailAPIView.as_view(), name='staffattendance-detail'),

    # Hostel Attendance
    path('hostel/', HostelAttendanceListCreateAPIView.as_view(), name='hostelattendance-list'),
    path('hostel/<uuid:pk>/', HostelAttendanceDetailAPIView.as_view(), name='hostelattendance-detail'),

    # Transport Attendance
    path('transport/', TransportAttendanceListCreateAPIView.as_view(), name='transportattendance-list'),
    path('transport/<uuid:pk>/', TransportAttendanceDetailAPIView.as_view(), name='transportattendance-detail'),
]
