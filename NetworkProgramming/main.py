# Сетевое программирование в Python. Модуль Socket. Создание клиент-серверного
import socket
from crypto_utils import encrypt, decrypt

HOST = "127.0.0.1"   # адрес, на котором слушает сервер
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"Сервер запущен на {HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Подключён клиент: {client_address}")

    welcome = "Добро пожаловать! Вы подключены к серверу-чату. Введите сообщение: "
    client_socket.send(encrypt(welcome))   # шифруем приветствие

    while True:
        data = client_socket.recv(4096)
        if not data:
            print(f"Клиент {client_address} отключился")
            break

        try:
            client_message = decrypt(data)          # расшифровываем
        except Exception as e:
            print(f"Не удалось расшифровать сообщение: {e}")
            break

        print(f"Сообщение клиента {client_address}: {client_message}")

        server_response = input("Ответ сервера: ")
        client_socket.send(encrypt(server_response))  # шифруем ответ

    client_socket.close()