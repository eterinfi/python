# filename: udp_client.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(10)
for data in ['Michael', 'Tracy', 'Sarah']:
	s.sendto(data, ('192.168.0.2', 6489))
	print s.recv(1024)
s.close()