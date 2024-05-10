from django.urls import path

from national_accreditation.views import (
    NationalListCreateApiView,
    NationalRetrieveApiView,
    ReviewAccreditation,
    ApproveAccreditation,
    RejectAccreditation,
)

urlpatterns = [
    path('', NationalListCreateApiView.as_view()),
    path('<int:pk>/', NationalRetrieveApiView.as_view()),
    path('<int:pk>/review/', ReviewAccreditation.as_view()),
    path('<int:pk>/approve/', ApproveAccreditation.as_view()),
    path('<int:pk>/reject/', RejectAccreditation.as_view()),
]
