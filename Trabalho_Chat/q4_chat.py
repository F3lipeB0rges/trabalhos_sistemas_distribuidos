from cryptography.fernet import Fernet
import socket
import threading

def generate_key():
    return Fernet.generate_key()

def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    # linha de código que faz com que a mensagem fique descriptografada 
    # decrypted_message = encrypted_message.decode()
    return decrypted_message

def receive_messages(conn, key):
    while True:
        encrypted_message = conn.recv(1024)
        if not encrypted_message:
            break
        message = decrypt_message(encrypted_message, key)
        print("Received:", message)
        broadcast_message(message, conn)

def broadcast_message(message, sender_conn):
    # envia a mensagem para todos os clientes, exceto para o remetente
    for client_conn in client_connections:
        if client_conn != sender_conn:
            encrypted_message = encrypt_message(message, client_keys[client_conn])
            client_conn.send(encrypted_message)

def handle_client(conn):
    key = generate_key()
    conn.send(key)

    with client_lock:
        client_connections.append(conn)
        client_keys[conn] = key

    receive_messages(conn, key)

    with client_lock:
        client_connections.remove(conn)
        del client_keys[conn]

    conn.close()

def chat_server():
    HOST = '127.0.0.1'
    PORT = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)

    print(f'Servidor escutando na porta {PORT}...')

    while True:
        conn, addr = s.accept()
        print("Conectado por ", addr)

        client_thread = threading.Thread(target=handle_client, args=(conn,))
        client_thread.start()

    s.close()

def chat_client():
    HOST = '127.0.0.1'
    PORT = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    key = s.recv(1024)

    receive_thread = threading.Thread(target=receive_messages, args=(s, key))
    receive_thread.start()

    while True:
        message = input("cliente: ")
        encrypted_message = encrypt_message(message, key)
        s.send(encrypted_message)
        if message.lower() == "sair":
            break

    s.close()

if __name__ == "__main__":
    client_connections = []
    client_keys = {}
    client_lock = threading.Lock()

    role = input("Você é o servidor(s) ou cliente(c)? ")

    if role.lower() == "s":
        chat_server()
    elif role.lower() == "c":
        chat_client()
    else:
        print("Opção inválida!!")
