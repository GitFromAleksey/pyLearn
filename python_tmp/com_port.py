import time
from time import sleep
import serial
from serial import tools
import serial.tools.list_ports

def main():

    # tls = tools
    # print(tls.list_ports.comports())
    # for item in serial.tools.list_ports.comports():
    #     print(item)

    # print('ser: ',ser)
    # print('ser.name',ser.name)
    # print('ser.BAUDRATE',ser.BAUDRATES)
    # print('ser.BYTESIZES',ser.BYTESIZES)
    # print('ser.is_open',ser.is_open)
    # print('ser.PARITIES',ser.PARITIES)
    # print('ser.portstr',ser.portstr)
    # print('ser.STOPBITS',ser.STOPBITS)
    # print('ser.timeout',ser.timeout)

    ser = serial.Serial('COM1', 9600, bytesize=8, parity='N', stopbits=1, timeout=1)

    ser.write(b'Hello com port')

    sleep(0.03)

    print("bytes in_waiting: ",ser.in_waiting)

    r = ser.read_all()

    print('ser.read(): ',r)

    ser.close()
    print('ser.is_open', ser.is_open)
    ser.__del__()

if __name__ == '__main__':
    main()




