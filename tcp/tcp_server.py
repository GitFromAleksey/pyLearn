import time
import socket
import threading


HOST = '127.0.0.1'
PORT = 8001 # https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers

class Server():

    def __init__(self, host = HOST, port = PORT):
        print(f'host: {host}, port: {port}')
        self.clients = []
        self.RcvEvtCb = None
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host,port))

    def Start(self):
        print(f'Start tcp server.')
        self.server.listen()
        thr = threading.Thread(target = self.Accepter, args = (self.server, self.clients))
        thr.start()

    def Stop(self):
        print(f'Stop tcp server.')
        self.server.close()

    def SetReceiveEventCallBack(self, rcv_evnt_cb):
        self.RcvEvtCb = rcv_evnt_cb

    def Accepter(self, server, clients):
        while True:
            try:
                client, address = server.accept()
                self.clients.append(client)
                print(f'Server new client: {client}, address: {address}')
                thr = threading.Thread(target = self.Receiver, args = (client, address))
                thr.start()
                self.BroadcastSend(f'New client accepted: {address}')
            except:
                pass

    def RemoveClient(self, client):
        print(f'Remove client: {client}\n')
        client.close()
        self.clients.remove(client)

    def BroadcastSend(self, msg):
        msg = 'Broadcast server message: ' + msg
        for client in self.clients:
            self.SendMsg(client, msg)

    def SendMsg(self, client, msg):
        try:
            client.send(msg.encode('utf-8'))
        except:
            print(f'SendMsg except')

    def Receiver(self, client, address):
        while True:            
            try:
                msg = client.recv(1024)
                if len(msg) > 0:
                    msg = msg.decode('utf-8')
                    print(f'Server receive from {address}: {msg}')
                    _ip, _port = client.getpeername()
                    if self.RcvEvtCb != None:
                        self.RcvEvtCb(ip = _ip,
                                      port = _port,
                                      message = msg)
                    self.SendMsg(client, msg)
                    self.BroadcastSend(f'{msg} from {address}')
                else:
                    self.RemoveClient(client)
                    break
                    
            except:
                self.RemoveClient(client)
                break

def ReceiveEvebtCallBack(**kwargs):
    print(f'ReceiveEvebtCallBack: {kwargs}')

def main():
    hname = socket.gethostname()
    print(hname)
    ip = socket.gethostbyname(hname)
    print(ip)
    ip = input('Enter server IP:')
    if len(ip) == 0:
        ip = HOST
    server = Server(host = ip, port = PORT)
    server.SetReceiveEventCallBack(ReceiveEvebtCallBack)
    server.Start()
    server.Stop()
    while True:
        time.sleep(1)
##        input()

if __name__ == '__main__':
    main()
