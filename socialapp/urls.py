from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
   # path('admin/', admin.site.urls),
    path('group',views.group,name='group'),
    path('chat/',views.index),
    path('creategroup/',views.creategroup.as_view(),name='creategroup'),
    path('chat/<str:room_name>/',views.room),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)