from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
   # path('admin/', admin.site.urls),
    path('chat/',views.index),
    path('chat/<str:room_name>/',views.room),

]