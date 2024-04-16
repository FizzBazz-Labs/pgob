from django.urls import path

from credentials.views import GenerateCredential

from national_accreditation.views import (
    NationalListCreateApiView,
    NationalRetrieveApiView,
    ReviewAccreditation,
    ApproveAccreditation,
    RejectAccreditation,
)

from national_accreditation.models import NationalAccreditation

urlpatterns = [
    path('', NationalListCreateApiView.as_view()),
    path('<int:pk>/', NationalRetrieveApiView.as_view()),
    path('<int:pk>/review/', ReviewAccreditation.as_view()),
    path('<int:pk>/approve/', ApproveAccreditation.as_view()),
    path('<int:pk>/reject/', RejectAccreditation.as_view()),
    path('<int:pk>/certificate/',
         GenerateCredential.as_view(model=NationalAccreditation)),
]
