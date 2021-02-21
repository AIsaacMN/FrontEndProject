from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de Usuario', required=True)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)