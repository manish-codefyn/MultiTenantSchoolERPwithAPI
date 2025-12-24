from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="MultiTenant School ERP API",
      default_version='v1',
      description="API documentation",
      contact=openapi.Contact(email="contact@schoolerp.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/v1/academics/', include('apps.academics.api.urls')),
    path('api/v1/admission/', include('apps.admission.api.urls')),
    path('api/v1/analytics/', include('apps.analytics.api.urls')),
    path('api/v1/assignments/', include('apps.assignments.api.urls')),
    # path('api/v1/attendance/', include('apps.attendance.api.urls')), # Not created
    path('api/v1/auth/', include('apps.auth.api.urls')),
    path('api/v1/communications/', include('apps.communications.api.urls')),
    path('api/v1/core/', include('apps.core.api.urls')),
    path('api/v1/events/', include('apps.events.api.urls')),
    path('api/v1/exams/', include('apps.exams.api.urls')),
    path('api/v1/finance/', include('apps.finance.api.urls')),
    path('api/v1/hostel/', include('apps.hostel.api.urls')),
    path('api/v1/hr/', include('apps.hr.api.urls')),
    path('api/v1/inventory/', include('apps.inventory.api.urls')),
    path('api/v1/library/', include('apps.library.api.urls')),
    path('api/v1/security/', include('apps.security.api.urls')),
    path('api/v1/students/', include('apps.students.api.urls')),
    path('api/v1/tenants/', include('apps.tenants.api.urls')),
    path('api/v1/transportation/', include('apps.transportation.api.urls')),
    path('api/v1/users/', include('apps.users.api.urls')),

    # Swagger
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
