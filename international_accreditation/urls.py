from django.urls import path

from international_accreditation.models import InternationalAccreditation

from international_accreditation.views import (
    InternationalListCreateApiView, InternationalRetrieveApiView,
    ReviewAccreditation,
    ApproveAccreditation,
    RejectAccreditation,
)

urlpatterns = [
    path('', InternationalListCreateApiView.as_view()),
    path('<int:pk>/', InternationalRetrieveApiView.as_view()),
    path('<int:pk>/review/', ReviewAccreditation.as_view()),
    path('<int:pk>/approve/', ApproveAccreditation.as_view()),
    path('<int:pk>/reject/', RejectAccreditation.as_view()),
]
