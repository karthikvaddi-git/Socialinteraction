from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from fundraise import views
urlpatterns = [
   path('fundraise',views.fundraiseposts,name='fundraise'),
   path('createfundraise',views.createfundraise.as_view(),name='createfundraise'),


   path('success',views.success,name='success')



]