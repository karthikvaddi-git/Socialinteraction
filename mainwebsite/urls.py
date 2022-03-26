from django.contrib import admin
from django.urls import path, include
from mainwebsite import views 
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('profile', views.show_profile, name='profile'),
    # path('createprofile',views.createprofile,name='createprofile')


    
    
    ]