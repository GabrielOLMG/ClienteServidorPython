from comandos import lista_comandos
from constantes import *

def verifica(msg,addr,conn,clientes_ativos):
    codigo = msg.split(" ")
    if codigo[0] == lista_comandos["DISCONNECT_MESSAGE"]:
        connected = False
        conn.send("CLOSE".encode(FORMAT))
        clientes_ativos[addr]["status"] = "offline"
    elif codigo[0] == lista_comandos["CLIENTES_ATIVOS"]:
        print(clientes_ativos)
        conn.send(" ".encode(FORMAT))
    elif codigo[0] == lista_comandos["CHANGE_NAME"]:
        print(f"{clientes_ativos[addr]['name']} mudou o nome para {codigo[1]}")
        clientes_ativos[addr]["name"] = codigo[1]
        conn.send(" ".encode(FORMAT))
    else:
        print(f"[{clientes_ativos[addr]['name']}] {msg}")
        conn.send(" ".encode(FORMAT))
    return