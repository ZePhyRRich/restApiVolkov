from cProfile import label
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from matplotlib import widgets
from . import models
from django import forms
from django.forms import ModelForm, TextInput, Textarea, FileInput, PasswordInput, ChoiceField, DateField


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {

            "username": TextInput(attrs={
                'class':'form-control',
                'placeholder':'Введите имя пользователя',
            }),

            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите email',
            }),

            "password1": PasswordInput(attrs={
                'type':'password',
                'class': 'form-control',
                'placeholder': 'Введите пароль',
            }),

            "password2": PasswordInput(attrs={
                'type':'password',
                'class': 'form-control',
                'placeholder': 'Подвтердите пароль',
            }),

        }


        


