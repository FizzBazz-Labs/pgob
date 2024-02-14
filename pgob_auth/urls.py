from django.urls import path, include

from pgob_auth import views


app_name = 'auth'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('auth/login/', views.SignInView.as_view(), name='login'),
    path('auth/logout/', views.SignOutView.as_view(), name='logout'),
    
    path('home/', views.HomeView.as_view(), name='home')
]
