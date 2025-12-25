from django.urls import path
from apps.assignments.api.views import (
    AssignmentListCreateAPIView, AssignmentDetailAPIView,
    SubmissionListCreateAPIView, SubmissionDetailAPIView
)

urlpatterns = [
    # Assignments
    path('', AssignmentListCreateAPIView.as_view(), name='assignment-list'),
    path('<uuid:pk>/', AssignmentDetailAPIView.as_view(), name='assignment-detail'),

    # Submissions
    path('submissions/', SubmissionListCreateAPIView.as_view(), name='submission-list'),
    path('submissions/<uuid:pk>/', SubmissionDetailAPIView.as_view(), name='submission-detail'),
]
