from django.urls import path

from credentials.views import TestTemplate


urlpatterns = [
    path('test-template/', TestTemplate.as_view(), name='test-template'),
]
