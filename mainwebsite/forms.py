from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from Accounts.models import *
from django.forms import ModelForm
from django import forms

        
class fundraiserform(ModelForm):
    class Meta:
        model = fundraiser
        fields = ('title','image','description','amount',)
class Postform(ModelForm):
    class Meta:
        model = Userpost
        fields = ('title','image','description',)