import time
import socket
import threading
import re
import subprocess

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
##                self.BroadcastSend(f'New client accepted: {address}')
            except:
                pass

    def RemoveClient(self, client):
        print(f'Remove client: {client}\n')
        client.close()
        self.clients.remove(client)

    def BroadcastSend(self, msg):
##        msg = 'Broadcast server message: ' + msg
        for client in self.clients:
            self.SendMsg(client, msg)

    def SendMsg(self, client, msg):
        try:
##            print(f'SendMsg: {client}, {msg}')
            client.send(msg.encode('utf-8'))
        except:
            print(f'SendMsg except')

    def Receiver(self, client, address):
        while True:            
            try:
                msg = client.recv(1024)
##                if len(msg) > 0:
                if msg:
                    msg = msg.decode('utf-8')
##                    print(f'Server receive from {address}: {msg}')
                    _ip, _port = client.getpeername()
                    if self.RcvEvtCb != None:
                        self.RcvEvtCb(ip = _ip,
                                      port = _port,
                                      message = msg)
##                    self.SendMsg(client, msg)
##                    self.BroadcastSend(f'{msg} from {address}')
                else:
                    self.RemoveClient(client)
                    break
                    
            except ConnectionResetError:
                print(f'Server Receiver except')
                self.RemoveClient(client)
                break

    def GetIpAddressesOfThisPc():
        ''' return all ip addresses on this pc '''
        ip_string_pattern = re.compile('IPv4-')
        ip_pattern = re.compile('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')

        result = subprocess.check_output('ipconfig', shell=True, text=True)
        text_lines = result.splitlines()

        ip_addresses = []

        for line in text_lines:
            ip_string_search_res = re.search(ip_string_pattern, line)
            if ip_string_search_res:
                ip_string = ip_string_search_res.string
                ip_search_res = re.search(ip_pattern, ip_string)
                if ip_search_res:
                    ip_addresses.append(ip_search_res.group())

        return ip_addresses


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

    while True:
        time.sleep(1)
##        if input() == 'q':
##            break
    server.Stop()


if __name__ == '__main__':
    main()
