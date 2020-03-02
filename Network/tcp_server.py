from socket import *
# 创建套接字
sockfd = socket()
# 绑定地址
sockfd.bind(('0.0.0.0', 8889))
# 设置监听
sockfd.listen(5)
# 等待接收连接
print("等待连接。。。。")
connfd, addr = sockfd.accept()
print("已连接到", addr)
# 收发消息
data = connfd.recv(1024)
print('服务端收到的data：', data.decode())
str = "我收到了你的消息{}".format(addr)
n = connfd.send(str.encode())
connfd.close()
sockfd.close()
