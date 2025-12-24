from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'librarys', views.LibraryViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'publishers', views.PublisherViewSet)
router.register(r'bookcategorys', views.BookCategoryViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'bookcopys', views.BookCopyViewSet)
router.register(r'bookissues', views.BookIssueViewSet)
router.register(r'reservations', views.ReservationViewSet)
router.register(r'fines', views.FineViewSet)
router.register(r'finepayments', views.FinePaymentViewSet)
router.register(r'librarymembers', views.LibraryMemberViewSet)
router.register(r'libraryreports', views.LibraryReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
