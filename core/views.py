import requests
from django import forms
from django.shortcuts import redirect, render
from django.views import View

import util
from .forms import LoginForm, RegisterForm

# Create your views here.
class LoginView(View):

    template_name = "core/login.html"

    def get(self, request, *args, **kwargs):
        form = LoginForm()

        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        
        if form.is_valid():
            # Obtener datos conforme al Form :  form.cleaned_data['username']  por ejemplo
            return redirect('/dashboard')

        return render(request, self.template_name, {'form':form})

class HomeView(View):

    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        
        return render(request, self.template_name)

class RegisterView(View):

    template_name = "core/register.html"

    def get(self, request, *args, **kwargs):
        form = RegisterForm()

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)

        if form.is_valid():
            data = {
                "name": form.cleaned_data['name'],
                "email": form.cleaned_data['email'],
                "username": form.cleaned_data['username'],
                "password": form.cleaned_data['password']
            }
            response = requests.post(f'{util.MONGO_URI}/api/users', json=data)
            print(response)
            return redirect('/dasboard')

        return render(request, self.template_name, {'form': form})