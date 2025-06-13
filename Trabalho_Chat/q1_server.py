import socket

HOST = '127.0.0.1' 
PORT = 12345  # Porta

# cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

# define o limite máximo de conexões simultâneas
s.listen(1)

print(f'Servidor escutando na porta {PORT}...')

# aguarda uma conexão
conn, addr = s.accept()
print(f'Conectado por {addr}')

# aguarda uma mensagem do cliente
data = conn.recv(1024)
print(f'Cliente: {data.decode()}')

conn.sendall('Eu recebi sua mensagem, cliente'.encode())

conn.close()