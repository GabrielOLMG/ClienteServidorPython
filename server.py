import socket 
import threading
from comandos import lista_comandos

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
clientes_ativos = {}

def verifica(msg,addr,conn):
    if msg == lista_comandos["DISCONNECT_MESSAGE"]:
        connected = False
        conn.send("CLOSE".encode(FORMAT))
        clientes_ativos[addr] = "offline"
    elif msg == lista_comandos["CLIENTES_ATIVOS"]:
        print(clientes_ativos)
    else:
        print(f"[{addr}] {msg}")
        conn.send("Msg received".encode(FORMAT))
                

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            thread = threading.Thread(target=verifica, args=(msg,addr, conn))
            thread.start()
            thread.join()

    conn.close()
        

def start():
    server.listen()
    
    print(f"[LISTENING] Server is listening on {SERVER}")    
    while True:
        conn, addr = server.accept()
        clientes_ativos[addr] = "online"
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()
