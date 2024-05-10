from django.urls import path

from core.views import SiteConfigurationView

urlpatterns = [
    path('config/', SiteConfigurationView.as_view()),
]
