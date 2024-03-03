from django.urls import path

from allergies.views import AllergiesListApiView

app_name = 'allergies'

urlpatterns = [
    path('allergies/',
         AllergiesListApiView.as_view(), name='list-create'),
]
