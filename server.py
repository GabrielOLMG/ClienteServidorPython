import socket 
import threading
from verifica_input import verifica
from constantes import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
clientes_ativos = {}


                

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            verifica(msg,addr,conn,clientes_ativos)
    conn.close()
        

def start():
    server.listen()
    
    print(f"[LISTENING] Server is listening on {SERVER}")    
    while True:
        conn, addr = server.accept()
        clientes_ativos[addr] = {"status":"online","name":"Cliente " + str(len(clientes_ativos))}
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()
