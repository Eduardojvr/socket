import socket
import subprocess

host = "127.0.0.1"
port = 2525

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen(2)

while True:
    msg = input("Shell >>")
    c, e = s.accept()
    print("Conectado com ", e)
    c.send(msg.encode())    
    m = c.recv(1024)
    print(m)
    c.close()
