"""
ASGI config for socialinteraction project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path,include
from django.core.asgi import get_asgi_application
import socialapp.routing
from django.core.asgi import get_asgi_application
import call.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socialinteraction.settings')

application = get_asgi_application()


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
          socialapp.routing.websocket_urlpatterns,


        )
    )
})