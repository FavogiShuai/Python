from socket import *

s = socket()
s.bind(('0.0.0.0', 8666))
s.listen(5)
while True:
    c, addr = s.accept()
    print("connect from", addr)
    data = c.recv(4096)
    print('***********************')
    print(data.decode())
    print('***********************')
    data = '''HTTP/1.1 200 OK
    Content-EnCoding:gzip
    Content-Type:text/html
    
    <h1>Hello World</h1>
    '''
    c.send(data.encode())
    c.close()
s.close()

