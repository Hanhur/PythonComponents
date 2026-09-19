import socket
from crypto_utils import encrypt, decrypt

HOST = "127.0.0.1"   # если сервер на другой машине — впиши её IP
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

server_message = decrypt(client_socket.recv(4096))
print(server_message)

while True:
    client_message = input("Введите сообщение: ")

    if not client_message:
        print("Отключаюсь...")
        break

    client_socket.send(encrypt(client_message))

    data = client_socket.recv(4096)
    if not data:
        print("Сервер закрыл соединение.")
        break

    server_response = decrypt(data)
    print(f"Ответ сервера: {server_response}")

client_socket.close()