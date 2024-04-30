from django.urls import path

from countries.views import CountriesListApiView

urlpatterns = [
    path('countries/', CountriesListApiView.as_view()),
]
