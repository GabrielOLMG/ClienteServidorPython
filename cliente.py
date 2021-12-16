import socket
from comandos import lista_comandos

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
conectado = True


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    if client.recv(2048).decode(FORMAT) == "CLOSE":
        print("finalizado")
        return False
    else:
        return True


while conectado:
    mensagem = input()
    conectado = send(mensagem)

