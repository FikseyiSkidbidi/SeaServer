# server.py
import socket
import threading

HOST = '127.0.0.1' # Поставь IP своего ПК для игры по сети
PORT = 65432

def handle_client(conn, addr, other_conn):
    try:
        while True:
            data = conn.recv(1024)
            if not data: break
            if other_conn:
                other_conn.sendall(data) # Пересылаем ход сопернику
    except:
        pass
    finally:
        conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(2)
    print("Сервер запущен. Ожидание игроков...")

    clients = []
    while len(clients) < 2:
        conn, addr = server.accept()
        print(f"Подключился: {addr}")
        clients.append(conn)
        
    print("Оба игрока подключены. Игра начинается!")
    threading.Thread(target=handle_client, args=(clients[0], clients[0].getpeername(), clients[1])).start()
    threading.Thread(target=handle_client, args=(clients[1], clients[1].getpeername(), clients[0])).start()

if __name__ == "__main__":
    start_server()