import socket
s = socket.socket()
port = 5500

s.connect(('localhost', port))
running = True
while running:
    raw = input("enter message: ").split(' ')
    payload = ""
    if raw[0] == 'exit':
        running = False
        break
    else:
        for i in range(len(raw)):
            payload += ' ' + raw[i]
        
        s.sendall(payload.encode())

s.close()