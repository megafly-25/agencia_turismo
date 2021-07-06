from django.contrib.auth import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegister(UserCreationForm):
    email=forms.EmailField()
    celular=forms.IntegerField()
    password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirma Contraseña',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','email','celular','password1','password2']
        help_texts={k:"" for k in fields}