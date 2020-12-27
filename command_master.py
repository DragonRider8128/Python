import time
import sys
import socket
import os

#Connect to slave
s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
print("Waiting for incoming connections...")
s.listen()
conn , addr = s.accept()
print(addr, "Connected to the server.")

#Send a command to run
command = input("Enter batch command: ")
conn.send(command.encode())
print("Command has been sent.")
data = conn.recv(1024)
if data:
    print("Command has been recieved and will be executed in 5 seconds.")
