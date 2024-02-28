from django.urls import path

from core.views import *

app_name = 'core'

urlpatterns = [
    path('accreditations-list/', AccreditationListView.as_view(), name='accreditations_list'),

]
