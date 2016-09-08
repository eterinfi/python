import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.2', 6489))
print s.recv(1024)
for data in ['Michael', 'Tracy', 'Sarah']:
	s.send(data)
	print s.recv(1024)
s.send('exit')
s.close()