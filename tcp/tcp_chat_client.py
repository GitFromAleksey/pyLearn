from tcp_client import Client
##from tcp_server import Server
import time


HOST = '127.0.0.1'
PORT = 8001 # https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers

def ReceiveEvebtCallBack(**kwargs):
    print(f'\nReceiveEvebtCallBack: {kwargs}\n')

def main():

    ip = input('Enter server IP:')
    if len(ip) == 0:
        ip = HOST

    client = Client(host = ip, port = PORT)
    client.SetReceiveEventCallBack(ReceiveEvebtCallBack)

    client.Connect()

    while True:
        msg = input('Input message or "q" for exit :>> ')
        if  msg == 'q':
            break
        else:
            client.SendMsg(msg)

    client.Disconnect()
    

if __name__ == '__main__':
    main()
