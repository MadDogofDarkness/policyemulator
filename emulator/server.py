import socket
import sys
import qE

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 5500
s.bind(('localhost', port))
print(host)

s.listen(5)
while True:
    try:
        c, addr = s.accept()
        print('got connection from', addr)
        qE.add(addr)
        '''[(<socket.socket fd=672, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 5500), raddr=('127.0.0.1', 51384)>, ('127.0.0.1', 51384))]'''
        im = c.recv(2048)
        '''for client in clients:
            client send(im[0])'''
        print(im)
        print(qE.q)
        c.close()
    except ConnectionAbortedError:
        print("connection aborted")
