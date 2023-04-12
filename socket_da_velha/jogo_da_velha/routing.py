from django.conf.urls import url
from jogo_da_velha.consumers import JogoDaVelhaConsumer

websocket_urlpatterns = [
    url(r'^ws/play/(?P<room_code>\w+)/$', JogoDaVelhaConsumer.as_asgi()),
]
