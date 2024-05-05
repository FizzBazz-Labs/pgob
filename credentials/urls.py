from django.urls import path

from credentials.views import TestTemplate, TestWeaponAccreditation, GenerateAccreditationView

urlpatterns = [
    path('test-template/', TestTemplate.as_view(), name='test-template'),
    path('test-weapon-accreditation/', TestWeaponAccreditation.as_view(),
         name='test-weapon-accreditation'),

    path('pillow/', GenerateAccreditationView.as_view())
]
