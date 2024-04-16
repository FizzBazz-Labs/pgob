from django.urls import path

from core.views import SiteConfigurationView, AccreditationListView

urlpatterns = [
    path('config/', SiteConfigurationView.as_view()),

    path('accreditations/', AccreditationListView.as_view()),
]
