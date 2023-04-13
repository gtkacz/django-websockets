from django.conf.urls import url

from game.consumers import JogoDaVelhaConsumer

websocket_urlpatterns = [
    url(r'^ws/play/(?P<room_code>\w+)/$', JogoDaVelhaConsumer.as_asgi()),
]