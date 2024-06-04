from django.urls import path

from .views import HelpSectionListView

urlpatterns = [
    path('', HelpSectionListView.as_view()),
]
