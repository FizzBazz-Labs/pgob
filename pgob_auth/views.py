from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView


class SignInView(LoginView):
    template_name = 'pgob_auth/login.html'
    success_url = reverse_lazy('auth:home')


class SignOutView(LoginRequiredMixin, LogoutView):
    ...
    

class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        return redirect(reverse_lazy('core:home'))

