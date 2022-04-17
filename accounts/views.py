from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout

class SignupView(TemplateView):
    template_name = 'accounts/signup.html'

    def post(self, request, *args, **kwargs):
        
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'accounts/signup.html',{'error':'このユーザーは既に登録されています。'})
        return redirect('accounts:login')


class LoginView(TemplateView):
    template_name = 'accounts/login.html'
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('exam:index')
        else:
            return render(request, 'accounts/login.html',{'error':'ログインできませんでいした。'})

class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = "accounts/login.html"