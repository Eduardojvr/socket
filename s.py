import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "" #127.0.0.1
porta = 8291

msg = "Hello World!"

s.bind((host, porta))
s.listen(1)

while True:
	c, e = s.accept()
	print("Conectado com ", e)
	c.send(msg.encode('ascii'))
	c.close()
