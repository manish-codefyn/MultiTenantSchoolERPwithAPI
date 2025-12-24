from django.urls import path, include
from django.conf import settings

API_PREFIX = f"api/{settings.API_VERSION}/"

urlpatterns = [
    path(f"{API_PREFIX}tenants/", include("apps.tenants.api.urls")),
    path(f"{API_PREFIX}users/", include("apps.users.api.urls")),
    path(f"{API_PREFIX}core/", include("apps.core.api.urls")),
    path(f"{API_PREFIX}auth/", include("apps.auth.api.urls")),
    path(f"{API_PREFIX}security/", include("apps.security.api.urls")),
    path(f"{API_PREFIX}academics/", include("apps.academics.api.urls")),
    path(f"{API_PREFIX}admission/", include("apps.admission.api.urls")),
    path(f"{API_PREFIX}analytics/", include("apps.analytics.api.urls")),
    path(f"{API_PREFIX}communications/", include("apps.communications.api.urls")),
    path(f"{API_PREFIX}events/", include("apps.events.api.urls")),
    path(f"{API_PREFIX}exams/", include("apps.exams.api.urls")),
    path(f"{API_PREFIX}finance/", include("apps.finance.api.urls")),
    path(f"{API_PREFIX}hostel/", include("apps.hostel.api.urls")),
    path(f"{API_PREFIX}hr/", include("apps.hr.api.urls")),
    path(f"{API_PREFIX}inventory/", include("apps.inventory.api.urls")),
    path(f"{API_PREFIX}library/", include("apps.library.api.urls")),
    path(f"{API_PREFIX}students/", include("apps.students.api.urls")),
    path(f"{API_PREFIX}transportation/", include("apps.transportation.api.urls")),
    path(f"{API_PREFIX}assignments/", include("apps.assignments.api.urls")),
]
