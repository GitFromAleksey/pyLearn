import serial
import serial.tools
import serial.tools.list_ports
import time

print('Stm32 com port test.\n')

def main():
    portName = 'COM9'
    port = serial.Serial()

    port.setPort(portName)
    port.baudrate = port.BAUDRATES[13]

    try:
        port.open()
        # while True:

        # port.write(b'Hello from PC to STM32\r\n')
        port.write([0x1B, 0x01, 0x00, 0x00])
        time.sleep(1)
        print(port.read(port.inWaiting()))
    except IOError:
        print('IOError: Port closing')
        port.close()
    finally:
        print('finally: Port closing')
        port.close()



if __name__ == '__main__':
    main()