import telnetlib
import getpass

HOST_DIR_615 = '192.168.0.112'
LOGIN_DIR_615 = 'admin'
PASSW_DIR_615 = 'admin1'

HOST_DIR_300 = '192.168.0.1'
LOGIN_DIR_300 = 'admin'
PASSW_DIR_300 = 'admin2'

PORT = 23
TIMEOUT = 10


# passw = getpass.getpass()
# print(passw)

def TelnetReboot(_host=None, _login='', _password='', _port=PORT):
    tel_net = telnetlib.Telnet(host=_host, port=_port)
    login = tel_net.read_until(b'login: ')
    print(login)
    tel_net.write(_login.encode('ascii')  +b'\n')
    password = tel_net.read_until(b'Password: ')
    print(password)
    tel_net.write(_password.encode('ascii')  +b'\n')
    # tel_net.write(b'cd ..\n')
    tel_net.write(b'ls\n')
    tel_net.write(b'reboot\n')
    tel_net.write(b'exit\n')
    w = tel_net.read_all()
    print(w.decode('ascii'))

def main():
    TelnetReboot(HOST_DIR_300, LOGIN_DIR_300, PASSW_DIR_300)
    TelnetReboot(HOST_DIR_615, LOGIN_DIR_615, PASSW_DIR_615)

if __name__ == '__main__':
    main()