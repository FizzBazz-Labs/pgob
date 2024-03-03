from django.urls import path

from countries.views import CountriesListApiView

app_name = 'countries'

urlpatterns = [
    path('countries/',
         CountriesListApiView.as_view(), name='list-create'),
]
