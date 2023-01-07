import time
import socket
import threading


HOST = '127.0.0.1'
PORT = 8001 # https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers

class Server():

    def __init__(self, host = HOST, port = PORT):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host,port))
        self.server.listen()
        self.clients = []
        thr = threading.Thread(target = self.Accepter, args = (self.server, self.clients))
        thr.start()

    def Accepter(self, server, clients):
        while True:
            try:
                client, address = server.accept()
                clients.append(client)
##                print(f'Server new client: {client}, address: {address}')
##                self.SendMsg(client, 'Connection accepted!!!'.encode('utf-8'))
                thr = threading.Thread(target = self.Receiver, args = (client, address))
                thr.start()
            except:
                pass

    def BroadcastSend(self, msg):
        msg = msg.encode('utf-8')
        for client in self.clients:
            SendMsg(self, client, msg)

    def SendMsg(self, client, msg):
        client.send(msg.encode('utf-8'))

    def Receiver(self, client, address):
        while True:            
            try:
                msg = client.recv(1024)
                if len(msg) > 0:
                    msg = msg.decode('utf-8')
                    print(f'Server receive from {address}: {msg}')
##                    self.SendMsg(client, msg)
                    BroadcastSend(msg)
                else:
                    client.close()
                    self.clients.remove(client)
                    break
                    print(f'Server close client: {client}\n')
            except:
                client.close()
                self.clients.remove(client)
                break
                pass

def main():

    server = Server(host = HOST, port = PORT)
    

if __name__ == '__main__':
    main()
