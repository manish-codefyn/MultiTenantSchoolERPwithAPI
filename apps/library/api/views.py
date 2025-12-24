from rest_framework import viewsets
from apps.core.api.permissions import TenantAccessPermission, RoleRequiredPermission
from rest_framework.permissions import IsAuthenticated
from apps.core.permissions.mixins import TenantAccessMixin
from apps.library.models import *
from .serializers import *

class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'librarian', 'admin']

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'librarian', 'admin']

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'librarian', 'admin']

class BookCategoryViewSet(viewsets.ModelViewSet):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'librarian', 'admin']

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'librarian', 'admin']

class BookCopyViewSet(viewsets.ModelViewSet):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'librarian', 'admin']

class BookIssueViewSet(viewsets.ModelViewSet):
    queryset = BookIssue.objects.all()
    serializer_class = BookIssueSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'librarian', 'admin']

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'librarian', 'admin']

class FineViewSet(viewsets.ModelViewSet):
    queryset = Fine.objects.all()
    serializer_class = FineSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'librarian', 'admin']

class FinePaymentViewSet(viewsets.ModelViewSet):
    queryset = FinePayment.objects.all()
    serializer_class = FinePaymentSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'librarian', 'admin']

class LibraryMemberViewSet(viewsets.ModelViewSet):
    queryset = LibraryMember.objects.all()
    serializer_class = LibraryMemberSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'librarian', 'admin']

class LibraryReportViewSet(viewsets.ModelViewSet):
    queryset = LibraryReport.objects.all()
    serializer_class = LibraryReportSerializer
    permission_classes = [IsAuthenticated, TenantAccessPermission, RoleRequiredPermission]
    required_roles = ['teacher', 'student', 'librarian', 'admin']

