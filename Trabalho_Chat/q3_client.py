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

# conecta ao servidor
s.connect((HOST, PORT))

# recebe a chave de criptografia do servidor
key = s.recv(1024)

# envia uma mensagem para o servidor
message = 'Olá, servidor!'
encrypted_message = encrypt_message(message, key)
s.sendall(encrypted_message)

# aguarda uma resposta do servidor
data = s.recv(1024)
decrypted_data = decrypt_message(data, key)
print(f'Resposta do servidor: {decrypted_data}')

s.close()
