from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'eventcategorys', views.EventCategoryViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'eventregistrations', views.EventRegistrationViewSet)
router.register(r'eventdocuments', views.EventDocumentViewSet)
router.register(r'eventtasks', views.EventTaskViewSet)
router.register(r'eventexpenses', views.EventExpenseViewSet)
router.register(r'eventgallerys', views.EventGalleryViewSet)
router.register(r'galleryimages', views.GalleryImageViewSet)
router.register(r'eventfeedbacks', views.EventFeedbackViewSet)
router.register(r'recurringeventpatterns', views.RecurringEventPatternViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
