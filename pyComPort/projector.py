import time
import re
import serial
import serial.tools
import serial.tools.list_ports
import threading

PORT_DESCRIBTION = re.compile(r'Arduino Uno')


def GetArduinoPortName() -> str:
    port_name = None
    ports = serial.tools.list_ports.comports()

    for port in ports:
        if re.search(PORT_DESCRIBTION, port.description):
            # print('-'*80)
            # print(f'description:{port.description}')
            # print(f'device:{port.device}')
            # print(f'hwid:{port.hwid}')
            # print(f'interface:{port.interface}')
            # print(f'location:{port.location}')
            # print(f'name:{port.name}')
            # print(f'pid:{port.pid}')
            # print(f'product:{port.product}')
            # print(f'serial_number:{port.serial_number}')
            # print(f'manufacturer:{port.manufacturer}')
            # print(f'vid:{port.vid}')
            port_name = port.name

    return port_name

class Protocol(object):
    """\
    Protocol as used by the ReaderThread. This base class provides empty
    implementations of all methods.
    """

    def connection_made(self, transport):
        """Called when reader thread is started"""

    def data_received(self, data):
        """Called with snippets received from the serial port"""

    def connection_lost(self, exc):
        """\
        Called when the serial port is closed or the reader loop terminated
        otherwise.
        """
        if isinstance(exc, Exception):
            raise exc

class ArduiniProtocol(Protocol):

    def __init__(self) -> None:
        self.rx_data = ''
        self.rx_counter = 0
        self.transport = None

    def connection_made(self, transport):
        """Called when reader thread is started"""
        self.transport = transport
        print(f'connection_made')

    def data_received(self, data):
        """Called with snippets received from the serial port"""
        self.rx_data += data.decode('ascii')
        if self.rx_data.find("\n") > -1:
            self.rx_data = self.rx_data.replace("\r\n","")
            print(f'{self.rx_counter}: rx_data:{self.rx_data}')
            self.rx_data = ''
            self.rx_counter += 1
            if self.transport:
                # data_str = 'SDgz'
                # data = str.encode(data_str)
                # serial_thr.write(data)
                self.transport.write(b'data_received')

    def connection_lost(self, exc):
        """\
        Called when the serial port is closed or the reader loop terminated
        otherwise.
        """
        print(f'connection_lost')
        if isinstance(exc, Exception):
            raise exc

class ArduinoSerialThread(threading.Thread):

    PORT_DESCRIBTION = re.compile(r'Arduino Uno')

    # def __init__(self, serial_instance, protocol: Protocol):
    def __init__(self, protocol: Protocol):
        super(ArduinoSerialThread, self).__init__()
        self.alive = False
        self.serial = self.GetSerialInstance() # serial_instance
        self.protocol = protocol
        self.protocol.connection_made(self)
        self._connection_made = threading.Event()
        self._lock = threading.Lock()

    def GetSerialInstance(self):
        describtion = ArduinoSerialThread.PORT_DESCRIBTION
        port_name = None
        ports = serial.tools.list_ports.comports()

        for port in ports:
            if re.search(describtion, port.description):
                port_name = port.name

        if port_name:
            serial_port = serial.Serial()
            serial_port.port = GetArduinoPortName()
            serial_port.baudrate = serial_port.BAUDRATES[12] # 9600
            serial_port.open()
            return serial_port

        return None

    def stop(self):
        """Stop the reader thread"""
        self.alive = False
        if hasattr(self.serial, 'cancel_read'):
            self.serial.cancel_read()
        self.join(2)

    def write(self, data):
        """Thread safe writing (uses lock)"""
        with self._lock:
            return self.serial.write(data)

    def run(self):
        """Reader loop"""
        if not hasattr(self.serial, 'cancel_read'):
            self.serial.timeout = 1

        error = None
        self._connection_made.set()
        self.alive = True
        while self.alive and self.serial.is_open:
            try:
                # read all that is there or wait for one byte (blocking)
                data = self.serial.read(self.serial.in_waiting or 1)
            except serial.SerialException as e:
                # probably some I/O problem such as disconnected USB serial
                # adapters -> exit
                error = e
                break
            else:
                if data:
                    # make a separated try-except for called user code
                    try:
                        self.protocol.data_received(data)
                    except Exception as e:
                        error = e
                        break
        # self.alive = False
        self.protocol = None
        print('run exit')

    # def __enter__(self):
    #     """\
    #     Enter context handler. May raise RuntimeError in case the connection
    #     could not be created.
    #     """
    #     self.start()
    #     self._connection_made.wait()
    #     if not self.alive:
    #         raise RuntimeError('connection_lost already called')
    #     return self.protocol

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Leave context: close port"""
        self.close()

def main():

    protocol = ArduiniProtocol()
    serial_thr = ArduinoSerialThread(protocol)
    serial_thr.start()
    while serial_thr.is_alive():
        time.sleep(1)
        # data_str = 'SDgz'
        # data = str.encode(data_str)
        # serial_thr.write(data)
    serial_thr.stop()

    return

    serial_port = serial.Serial()
    serial_port.port = GetArduinoPortName()
    serial_port.baudrate = serial_port.BAUDRATES[12] # 9600
    serial_port.open()

    protocol = Protocol()

    st = ArduinoSerialThread(serial_port, protocol)
    st.start()

# self.transport.write(text.encode(self.ENCODING, self.UNICODE_HANDLING) + self.TERMINATOR)
    text = b'to arduino'
    st.write(text)
    time.sleep(10)

    st.stop()
    return

    port_name = GetArduinoPortName()
    print(port_name)
    serial_port = serial.Serial()
    serial_port.port = port_name
    serial_port.baudrate = serial_port.BAUDRATES[12] # 9600
    serial_port.open()
    while True:
        if serial_port.in_waiting > 0: # if serial_port.is_open:
            rx_bytes = serial_port.readline() # serial_port.read_all()
            print(rx_bytes.decode('ascii').replace('\n',''))
            # rx_data = serial_port.readline()
            print()
        else:
            time.sleep(0.1)
    serial_port.close()

if __name__ == '__main__':
    main()