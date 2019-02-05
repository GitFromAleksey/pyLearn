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
        while True:
            print(port.read(port.inWaiting()))
            port.write(b'Hello from PC to STM32\r\n')
            time.sleep(0.5)
    except IOError:
        print('IOError: Port closing')
        port.close()
    finally:
        print('finally: Port closing')
        port.close()



if __name__ == '__main__':
    main()