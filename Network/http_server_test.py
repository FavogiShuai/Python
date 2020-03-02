from socket import *


def handleClient(connfd):
    request = connfd.recv(1024)
    print(request.decode())

    try:
        f = open('./index.html')
    except IOError:
        response = "HTPP/1.1 404 not found\n"
        response += "\n"
        response += "Not Found!!!"
    else:
        response = "HTPP/1.1 200 OK\n"
        response += "\n"
        response += f.read()
    finally:
        connfd.send(response.encode())

def create_socket():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(('0.0.0.0', 8888))
    sockfd.listen(3)
    while True:
        connfd, addr = sockfd.accept()
        # 处理请求
        handleClient(connfd)
        connfd.close()
    socket.close()

if __name__ == '__main__':
    create_socket()