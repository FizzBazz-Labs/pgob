from django.urls import path

from profiles import views


app_name = 'auth'

urlpatterns = [
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('register/', views.UserRegister.as_view(), name='register'),
]
