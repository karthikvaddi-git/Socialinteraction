from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from Accounts.models import *
from django.forms import ModelForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email','phone',)