from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django.forms import ModelForm
from django import forms
        
class groupform(ModelForm):
    class Meta:
        model = Groupdata
        fields = ('groupname','image','description','tags',)

