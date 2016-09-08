import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('flash.weather.com.cn', 80))
s.send('GET /wmaps/xml/china.xml HTTP/1.1\r\nHost: flash.weather.com.cn\r\nConnection: close\r\n\r\n')
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)
s.close()
header, xml = data.split('\r\n\r\n', 1)
print header
with open('weather.xml', 'wb') as f:
    f.write(xml)
