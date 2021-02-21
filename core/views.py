from django.http.response import HttpResponseRedirect
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
            data = {
                "username": form.cleaned_data['username'],
                "password": form.cleaned_data['password']
            }
            response = requests.post(f"{util.MONGO_URI}/api/users/login", json=data)

            if response.status_code == 200:
                response = response.json()
                request.session[util.SESSION_USER] = {
                    "username": response['data']['username'],
                    "user_id": response['data']['_id']
                }

                return redirect('/groups')

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
            if response.status_code == 200:
                response = response.json()
                request.session[util.SESSION_USER] = {
                    "username": response['data']['username'],
                    "user_id": response['data']['_id']
                }

                return redirect('/groups')

        return render(request, self.template_name, {'form': form})

class GroupListView(View):
    
    template_name = "core/dashboard.html"

    def get(self, request, *args, **kwargs):
        try:
            temp_session = request.session[util.SESSION_USER]

            response = requests.get(f"{util.MONGO_URI}/api/groups/list/{temp_session['user_id']}")
            print(temp_session['user_id'])
            
            if response.status_code == 200:
                response = response.json()
                print(response)

                return render(request, self.template_name, {'groups': response['data']})

            raise KeyError

        except KeyError:
            return HttpResponseRedirect('/login')


    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)


class GroupView(View):
    
    def get(self, request, *args, **kawrgs):
        pass