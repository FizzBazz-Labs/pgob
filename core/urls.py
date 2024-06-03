from django.urls import path

from core.views import SiteConfigurationView, RetrievePowerBiToken

urlpatterns = [
    path('config/', SiteConfigurationView.as_view()),
    path('powerbi-token/<str:report_id>', RetrievePowerBiToken.as_view(), name='powerbi-token')
]
