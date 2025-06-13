import socket

HOST = '127.0.0.1' 
PORT = 12345  # Porta

# cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# conecta ao servidor
s.connect((HOST, PORT))

s.sendall('Olá, servidor! Eu sou o cliente'.encode())

# aguarda uma resposta do servidor
data = s.recv(1024)

print(f'Servidor: {data.decode()}')

s.close()
