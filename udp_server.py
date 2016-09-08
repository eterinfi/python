# filename: udp_server.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.0.2', 6489))
print 'Bind UDP on 6489...'
while True:
    data, addr = s.recvfrom(1024)
    print 'Received from %s:%s.' % addr
    s.sendto('Hello, %s!' % data, addr)