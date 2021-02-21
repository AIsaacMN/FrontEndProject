from django import forms
from django.shortcuts import redirect, render
from django.views import View

from .forms import LoginForm

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