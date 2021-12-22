from django.urls import path
from .consumers import *

websocket_urlpatterns = [
    path("api/v1/chat/", ChatJsonConsumer.as_asgi(), name="chat_socket"),
]
