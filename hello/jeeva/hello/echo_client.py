'''
Created on Mar 8, 2017

@author: jee11
'''

import socket


TCP_IP = '155.246.109.143'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World! mother fucker"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode('utf-8'))
data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:", data)