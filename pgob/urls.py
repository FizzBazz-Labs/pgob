from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

import rest_framework_simplejwt.views as jwt_views


urlpatterns = [
    # path('', include('core.urls')),
    path('auth/', include('pgob_auth.urls')),

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
    path("api/v1/", include("national_accreditation.urls")),
    path('api/v1/', include('overflight_non_commercial_aircraft.urls')),
    path('api/v1/', include('international_accreditation.urls')),
    path('api/v1/', include('security_accreditations.urls')),

]

urlpatterns = urlpatterns + \
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
