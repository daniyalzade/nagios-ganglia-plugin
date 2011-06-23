import socket

def netcat(hostname, port, content):
    """
    @param hostname: str
    @param port: int
    @param content: str
    @return data: str
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.sendall(content)
    s.shutdown(socket.SHUT_WR)
    data = ''
    while 1:
        cur_data = s.recv(1024)
        if cur_data == "":
            break
        data += str(cur_data)
    s.close()
    return data
