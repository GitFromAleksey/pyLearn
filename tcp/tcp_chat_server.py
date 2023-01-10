##from tcp_client import Client
from tcp_server import Server
import time


HOST = '127.0.0.1'
PORT = 8001 # https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers


def main():

    ip = input('Enter server IP:')
    if len(ip) == 0:
        ip = HOST

    server = Server(host = ip, port = PORT)
    server.Start()
##    client = Client(host = HOST, port = PORT)
##    client_1 = Client(host = HOST, port = PORT)

##    client.Connect()
##    client_1.Connect()

    while True:
        if input('q - exit :>> ') == 'q':
            break

##    client.Disconnect()
##    client_1.Disconnect()
    

if __name__ == '__main__':
    main()
