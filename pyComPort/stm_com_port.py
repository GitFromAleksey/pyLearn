import serial
import serial.tools
import serial.tools.list_ports
import time

print('Stm32 com port test.\n')

i2c_device_addr = 0x68

SELF_TEST_X = 0x0D # 0x4F - 0100 1111
SELF_TEST_Y = 0x0E # 0x4E - 0100 1110
SELF_TEST_Z = 0x0F # 0x97 - 1001 0111
SELF_TEST_A = 0x10 # 0x2d - 0010 1101
SMPLRT_DIV = 0x19

CONFIG = 0x1A
GYRO_CONFIG = 0x1B # 0x18 - 0001 1000

ACCEL_XOUT_H = 0x3B
ACCEL_XOUT_L = 0x3C
ACCEL_YOUT_H = 0x3D
ACCEL_YOUT_L = 0x3E
ACCEL_ZOUT_H = 0x3F
ACCEL_ZOUT_L = 0x40


TEMP_OUT_H = 0x41
TEMP_OUT_L = 0x42

GYRO_XOUT_H = 0x43
GYRO_XOUT_L = 0x44
GYRO_YOUT_H = 0x45
GYRO_YOUT_L = 0x46
GYRO_ZOUT_H = 0x47
GYRO_ZOUT_L = 0x48

USER_CTRL = 0x6A
PWR_MGMT_1 = 0x6B
PWR_MGMT_2 = 0x6C

WHO_AM_I = 0x75

def main():
    portName = 'COM3'
    port = serial.Serial()

    port.setPort(portName)
    port.baudrate = port.BAUDRATES[13]

    try:
        REG_VALUE = ACCEL_XOUT_L
        BYTES_TO_READ = 0x01
        WRITE_DATA = 0x00
        RD_WR_FLAG = 0x00
        
        port.open()
        # while True:

        # port.write(b'Hello from PC to STM32\r\n')
#         port.write([GYRO_CONFIG, 0x01, 0x00, 0x00])
        port.write([REG_VALUE, BYTES_TO_READ, WRITE_DATA, RD_WR_FLAG])
        time.sleep(0.1)
        
        data_in = port.read(port.inWaiting())
        
        print( hex(ord(data_in)) )
    except IOError:
        print('IOError: Port closing')
        port.close()
    finally:
        print('finally: Port closing')
        port.close()



if __name__ == '__main__':
    main()