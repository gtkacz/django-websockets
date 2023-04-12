"""
ASGI config for socket_da_velha project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""
import os

import jogo_da_velha.routing
from channels.auth import AuthMiddlewareStack
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socket_da_velha.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
    'http': AsgiHandler(),
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                jogo_da_velha.routing.websocket_urlpatterns
            ])
        )
    )
})

