import serial
import serial.tools
import serial.tools.list_ports
import time


print('__name__: ',__name__)

def main():
    print('Running main() function')
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(port)

    comPort = serial.Serial('COM1')
    comPort2 = serial.Serial('COM2')
    print('comPort.isOpen(): ',comPort.isOpen())
    print('comPort2.isOpen(): ',comPort2.isOpen())
    comPort.write(b'ATI\r')
    time.sleep(1)
    print('comPort2.read: ',comPort2.read(comPort2.in_waiting))

    comPort.close()

if __name__ == '__main__':
    main()
