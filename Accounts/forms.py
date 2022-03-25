from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from Accounts.models import *
from django.forms import ModelForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email','phone',)

class userintrest(ModelForm):
    class Meta:
        model = userprofile
        fields = ('intrests',)
        
class userprofile(ModelForm):
    class Meta:
        model = userprofile
        fields = ('name','profileimage','description','location','intrests',)