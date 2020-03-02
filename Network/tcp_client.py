from socket import *
socketfd = socket()
socketfd.connect(('192.168.2.186', 10089))
data = input(">>发送")
socketfd.send(data.encode())
data = socketfd.recv(1024)
print("客户端接收到：", data.decode())
socketfd.close()
