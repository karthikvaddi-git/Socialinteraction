from django.urls import path

from . import consumers

websocket_urlpatterns = [

    path('ws/call/', consumers.CallConsumer.as_asgi())

]