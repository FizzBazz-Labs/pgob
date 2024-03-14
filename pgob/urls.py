import rest_framework_simplejwt.views as jwt_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('api/v1/', include('core.urls')),
    # path('api/v1/', include('pgob_auth.urls')),

    path('admin/', admin.site.urls),

    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/docs/',
         SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),

    path('api/v1/auth/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token-obtain-pair'),
    path('api/v1/auth/token/refresh/',
         jwt_views.TokenRefreshView.as_view(), name='token-refresh'),
    path('api/v1/auth/token/verify/',
         jwt_views.TokenVerifyView.as_view(), name='token-verify'),

    path('api/v1/', include('core.urls')),
    path("api/v1/national-accreditations/",
         include("national_accreditation.urls")),
    path('api/v1/', include('overflight_non_commercial_aircraft.urls')),
    path('api/v1/international-accreditations/',
         include('international_accreditation.urls')),
    path('api/v1/', include('security_accreditations.urls')),
    path('api/v1/vehicle-access-airport-accreditations/',
         include('vehicle_access_airport_accreditations.urls')),
    path('api/v1/', include('intercom_equipment_declaration.urls')),
    path('api/v1/', include('general_vehicle_accreditation.urls')),
    path('api/v1/', include('vehicles.urls')),
    path('api/v1/', include('allergies.urls')),
    path('api/v1/', include('countries.urls')),
    path('api/v1/', include('immunizations.urls')),
    path('api/v1/', include('media_channels.urls')),
    path('api/v1/', include('medical_histories.urls')),
    path('api/v1/', include('positions.urls')),
    path('api/v1/', include('profiles.urls')),
    path('api/v1/', include('credentials.urls')),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
