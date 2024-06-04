from django.urls import path

from core.views import SiteConfigurationView, RetrievePowerBiToken, ReportApiListView

urlpatterns = [
    path('config/', SiteConfigurationView.as_view()),
    path('powerbi-token/<str:report_id>',
         RetrievePowerBiToken.as_view(), name='powerbi-token'),
    path('powerbi-reports/', ReportApiListView.as_view(), name='powerbi-reports')
]
