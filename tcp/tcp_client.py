import time
import socket
import threading


HOST = '127.0.0.1'
##HOST = '192.168.1.30'
PORT = 8001 # https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers


class Client():

    def __init__(self, host = HOST, port = PORT):
        self.SERVER = (host,port)
        self.client = None
         
    def SendMsg(self, msg):
        print(f'Sending message: "{msg}"')
        try:
            msg = msg.encode('utf-8')
            self.client.send(msg)
        except:
            print(f'SendMsg except')

    def Receiver(self):
        while True:
            try:
                msg = self.client.recv(1024)
                if len(msg) == 0:
                    continue
                msg = msg.decode('utf-8')
                print(f'Client receive: {msg}')
            except:
                self.Disconnect()
                print(f'Client Receiver break\n')
                break

    def Connect(self):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(self.SERVER)
            thr = threading.Thread(target = self.Receiver)
            thr.start()
        except socket.error as serr:
            print(f'Client connect error: {serr}')
        
    def Disconnect(self):
        self.client.close()

def main():
    ip = input('Enter server IP:')
    if len(ip) == 0:
        ip = HOST

    client = Client(host = ip)
    client.Connect()

    i = 10
    while i > 0:
        client.SendMsg(f'msg: {i}')
        time.sleep(1)
        i -= 1

    client.Disconnect()
    

if __name__ == '__main__':
    main()
