from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
   # path('admin/', admin.site.urls),
    path('group',views.group),
    path('chat/',views.index),
    path('creategroup/',views.creategroup),
    path('chat/<str:room_name>/',views.room),


]