import socket
import os
from threading import Thread
import sys


# Main class for receiving the information
class ProxyServerRecv(Thread):

    def __init__(self, host, port):
        super(ProxyServerRecv, self).__init__()
        self.client = None  # If there is no client.
        self.port = port
        self.host = host
        # Creates socket for server.
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connects to client.
        self.server.connect((host, port))

    def run(self):
        while True:
            data = self.server.recv(32768)

            if data:
                print("[Server Information] = {}".format(data.encode('hex')))
                self.client.sendall(data)


class ProxyClientRecv(Thread):

    def __init__(self, host, port):
        super(ProxyClientRecv, self).__init__()
        self.server = None  # if there is no server socket.
        self.port = port
        self.host = host
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, port))
        sock.listen(1)
        # Waiting for a connection
        self.game, addr = sock.accept()

    def run(self):
        while True:
            data = self.game.recv(4096)

            if data:
                print("[Client Information] = {}".format(data.encode('hex')))
                self.server.sendall(data)


class Proxy(Thread):

    def __init__(self, from_host, to_host, port):
        super(Proxy, self).__init__()
        self.from_host = from_host
        self.to_host = to_host
        self.port = port

    def run(self):

        while True:
            print("[Proxy is starting.. setting up {}]".format(self.port))
            self.pcr = ProxyClientRecv(self.from_host, self.port)  # Waiting for client
            self.psr = ProxyServerRecv(self.to_host, self.port)
            print("[Proxy has started... connection has been established on {}]".format(self.port))
            self.pcr.server = self.psr.server
            self.psr.client = self.pcr.client

            self.pcr.start()
            self.psr.start()


proxy_connection = Proxy('0.0.0.0', '192.168.178.54', 8888)
proxy_connection.start()

while True:
    try:
        cmd = input('$ ')
        if cmd[:4] == 'quit':
            exit()
    except Exception as e:
        print(e)
