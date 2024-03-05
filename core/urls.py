from django.urls import path

from core.views import *


urlpatterns = [
    path('accreditations/', AccreditationListView.as_view(), name='accreditations'),
]
