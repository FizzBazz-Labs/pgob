from django.urls import path

from credentials.views import TestTemplate


urlpatterns = [
    # path('generate-credential/<int:pk>/', GenerateCredential.as_view(),
    #      name='generate-credential'),
    path('test-template/', TestTemplate.as_view(), name='test-template'),
]
# Path: credentials/views.py
