from django.urls import path

from . import consumers
from call import consumers as s

websocket_urlpatterns = [
    path(r'ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
    path(r'ws/1/call/',s.CallConsumer.as_asgi())

]