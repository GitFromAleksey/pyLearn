import socket

localhost = '127.0.0.1'
PORT = 5051

SERVER = localhost, PORT

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind((localhost, PORT))
    print(f'sock.bind')
    msg = 'message text'.encode('utf-8')
    print(f'Sending message: "{msg.decode("utf-8")}"')
    sock.sendto(msg, SERVER)

    data, address = sock.recvfrom(1024)
    print(f'Received message: "{data.decode("utf-8")}" from address: {address}')

    


if __name__ == '__main__':
    main()
