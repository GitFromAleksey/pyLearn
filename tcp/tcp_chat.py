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
        self.client = None
        self.thr = threading.Thread(target = self.Accepter)
        self.thr.start()


    def Accepter(self):
        try:
            if self.client == None:
                self.client, self.address = self.server.accept()
                print(f'client: {self.client}, address: {self.address}')
                self.thr = threading.Thread(target = self.Receiver, args = (self.client,))
                self.thr.start()
        except:
            pass

    def Receiver(self, client):
        while True:            
            try:
                msg = client.recv(1024).decode('utf-8')
                print(f'msg: {msg}')        
            except:
                pass

class Client():

    def __init__(self, host = HOST, port = PORT):
        SERVER = (host,port)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host,port))

##        self.client.close()

    def SendMsg(self, msg):
        msg = msg.encode('utf-8')
        print(f'Sending message: "{msg.decode("utf-8")}"')
        self.client.send(msg)
        
        

def main():

    server = Server(host = HOST, port = PORT)
    client = Client(host = HOST, port = PORT)

    while True:
        client.SendMsg('msg')
        time.sleep(1)
    
    pass

if __name__ == '__main__':
    main()
