from cryptography.fernet import Fernet
import socket

def generate_key():
    return Fernet.generate_key()

def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

HOST = '127.0.0.1' 
PORT = 12345  # Porta

# cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# associa o objeto socket ao endereço e porta especificados
s.bind((HOST, PORT))

# define o limite máximo de conexões simultâneas
s.listen(1)

print(f'Servidor escutando na porta {PORT}...')

# aguarda uma conexão
conn, addr = s.accept()
print(f'Conectado por {addr}')

# gera a chave de criptografia
key = generate_key()

# envio a chave de criptografia para o cliente
conn.sendall(key)

# aguarda uma mensagem do cliente
data = conn.recv(1024)
decrypted_data = decrypt_message(data, key)
print(f'Mensagem recebida: {decrypted_data}')

# envia uma resposta para o cliente
response = 'Mensagem recebida com sucesso!'
encrypted_response = encrypt_message(response, key)
conn.sendall(encrypted_response)

conn.close()
