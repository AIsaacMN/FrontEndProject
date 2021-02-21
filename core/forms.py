from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de Usuario', required=True)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    name = forms.CharField(label="Nombre completo", required=True)
    email = forms.EmailField(label="Correo", required=True)
    username = forms.CharField(label='Nombre de Usuario', required=True)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)