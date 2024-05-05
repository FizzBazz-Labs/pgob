from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework.routers import DefaultRouter

import rest_framework_simplejwt.views as jwt_views

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from housing.views import HousingViewSet
from commerce.views import CommerceViewSet
from general_vehicle_accreditation.views import GeneralVehicleViewSet
from overflight_non_commercial_aircraft.views import OverflightNonCommercialAircraftViewSet
from vehicle_access_airport_accreditations.views import AirportVehicleAccessViewSet
from intercom_equipment_declaration.views import IntercomEquipmentDeclarationViewSet
from security_accreditations.views import SecurityWeaponViewSet

router = DefaultRouter()

router.register(r'housings', HousingViewSet)
router.register(r'commerces', CommerceViewSet)
router.register(r'general-vehicles', GeneralVehicleViewSet)
router.register(r'overflight-non-commercial-aircrafts',
                OverflightNonCommercialAircraftViewSet)
router.register(r'airport-vehicle-access', AirportVehicleAccessViewSet)
router.register(r'intercommunication-equipments',
                IntercomEquipmentDeclarationViewSet)
router.register(r'security-weapons', SecurityWeaponViewSet)

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
    path('api/v1/overflight-non-commercial-aircraft/',
         include('overflight_non_commercial_aircraft.urls')),
    path('api/v1/international-accreditations/',
         include('international_accreditation.urls')),
    path('api/v1/security-weapon-accreditation/',
         include('security_accreditations.urls')),
    path('api/v1/vehicle-access-airport-accreditations/',
         include('vehicle_access_airport_accreditations.urls')),
    path('api/v1/intercom-equipment-declaration/',
         include('intercom_equipment_declaration.urls')),
    path('api/v1/general-vehicle-accreditation/',
         include('general_vehicle_accreditation.urls')),
    path('api/v1/', include('vehicles.urls')),
    path('api/v1/', include('allergies.urls')),
    path('api/v1/', include('countries.urls')),
    path('api/v1/', include('immunizations.urls')),
    path('api/v1/', include('media_channels.urls')),
    path('api/v1/', include('medical_histories.urls')),
    path('api/v1/', include('positions.urls')),
    path('api/v1/', include('profiles.urls')),
    path('api/v1/', include('credentials.urls')),

    path('api/v1/', include(router.urls))
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
