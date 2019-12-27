import socket
# 获取计算机名
hostname = socket.gethostname()
print(hostname)

#
print(socket.gethostbyaddr('baidu'))

sockfd = socket.socket
sockfd.bind()