from django.urls import path

from pgob_auth import views

urlpatterns = [
    path('password/change', views.ChangePasswordView)
]
