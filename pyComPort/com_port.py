import serial
import serial.tools
import serial.tools.list_ports
import time


print('__name__: ',__name__)


def main():
    print('Running main() function')
    ports = serial.tools.list_ports.comports()
#     for port in ports:
#         print('port name:', port[0])
#         try:
#             comPort = serial.Serial('COM11',9600)
# #             comPort = serial.Serial(port[0],9600)
# #             comPort.baudrate = 9600#38400
#             if comPort.isOpen():
#                 comPort.write(b'AT\r\n')
#                 time.sleep(1)
#                 print(comPort.read(comPort.inWaiting()))
#                 comPort.close()
#             else:
#                 print('port: ', port, 'is not open')
#         except IOError:
#             print('IOError')
#         finally:
#             pass

    pcPortName = 'COM11'
    btPortName = 'COM12'

    pcPort = serial.Serial()
    btPort = serial.Serial()
    
    pcPort.setPort(pcPortName)
    pcPort.baudrate = pcPort.BAUDRATES[13]
    btPort.setPort(btPortName)
    btPort.baudrate = pcPort.BAUDRATES[12]

    pcPort.open()
    btPort.open()

    cnt = 0
    while cnt < 10:
        str_ = 'cnt = ' + str(cnt)
        cnt = cnt + 1
        pcPort.write(str.encode(str_))
        time.sleep(0.5)
        print(btPort.read(btPort.inWaiting()))

    pcPort.close()
    btPort.close()
#     comPort = serial.Serial('COM1')
#     comPort2 = serial.Serial('COM2')
#     print('comPort.isOpen(): ',comPort.isOpen())
#     print('comPort2.isOpen(): ',comPort2.isOpen())
#     comPort.write(b'ATI\r')
#     time.sleep(1)
#     print('comPort2.read: ',comPort2.read(comPort2.in_waiting))
  
#     comPort.close()

if __name__ == '__main__':
    main()
