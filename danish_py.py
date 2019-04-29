# -*- coding: utf-8 -*-
"""danish.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MH5p97iVGPk90gxjjpRiA7gDiqeYldqI
"""

#danish shehzad
#sp19-bsse-0006

import socket	#for sockets
import sys	#for exit

try:
	#create an AF_INET, STREAM socket (TCP)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.gaierror:
	print ('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
	sys.exit();

print ('Socket Created')

host = 'www.google.com'
port = 80

try:
	remote_ip = socket.gethostbyname( host )

except socket.gaierror:
	#could not resolve
	print ('Hostname could not be resolved. Exiting')
	sys.exit()
	
print ('Ip address of ' + host + ' is ' + remote_ip)

#Connect to remote server
s.connect((remote_ip , port))

print ('Socket Connected to ' + host + ' on ip ' + remote_ip)

#websitelinkcode
import pyautogui

pic= pyautogui.screenshot()

pic.save('screenshot.png')


