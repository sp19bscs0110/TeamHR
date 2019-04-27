#!/usr/bin/env python
# coding: utf-8

# In[ ]:
#Shahmeer
#Sp19bsse0007

import socket
s= socket.socket()
host=s.gethostname()
port= 8080
s.blind((host,port))
s.listen(1)
print("Waiting for any incoming connections...")
conn,addr = conn.accept()
print(addr,"Has connected to a server")

