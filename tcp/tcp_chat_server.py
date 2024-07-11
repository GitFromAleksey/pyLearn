from tcp_server import Server
# import time
# import json
# import urllib


HOST = '127.0.0.1'
PORT = 8001 # https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers

def ReceiveEvebtCallBack(**kwargs):
##    print(f'Server ReceiveEvebtCallBack: {kwargs}')
    print(f'Client ip: {kwargs["ip"]}')
    print(f'Client port: {kwargs["port"]}')
    print(f'Client message: {kwargs["message"]}')


def main():

    print(Server.GetIpAddressesOfThisPc())

    ip = input('Enter server IP:')
    if len(ip) == 0:
        ip = HOST

    server = Server(host = ip, port = PORT)
    server.SetReceiveEventCallBack(ReceiveEvebtCallBack)
    server.Start()

    while True:
##        if input('q - exit :>> ') == 'q':
##            break
        msg = input('Input message or "q" for exit :>> ')
        if  msg == 'q':
            break
        else:
            server.BroadcastSend(msg)

    server.Stop()

if __name__ == '__main__':
    main()
