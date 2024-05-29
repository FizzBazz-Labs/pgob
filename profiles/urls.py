from django.urls import path

from profiles import views

app_name = 'auth'

urlpatterns = [
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('register/', views.UserRegister.as_view(), name='register'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user'),

    path('profile/change-password/', views.ChangePasswordView.as_view()),
]
