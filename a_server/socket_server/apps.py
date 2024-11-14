from django.apps import AppConfig
from socket_server import server

import threading


class SocketServerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'socket_server'

    def ready(self):

        tcp_server = threading.Thread(target=server.main)
        tcp_server.setDaemon(True)
        tcp_server.start()

        return super().ready()
