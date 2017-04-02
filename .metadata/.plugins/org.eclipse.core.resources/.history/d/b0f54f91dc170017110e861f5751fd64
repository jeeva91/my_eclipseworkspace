'''
Created on Apr 1, 2017

@author: jee11
'''
from threading import Thread
from queue import Queue
from _overlapped import NULL
from _socket import socket
class Receiver_Thread(Thread):
    '''
    classdocs
    '''
    

    def __init__(self,received=Queue(0),rcv_socket=socket):
        '''
        Constructor
        '''
        self.receiver_switch="True"
        self.received=received
        self.rcv_socket=rcv_socket
        
    def run(self):
        pass
        self.receive()
    
    def receive(self):
        while(self.receiver_switch=="True"):
            pass
            data=self.rcv_socket.recv(1024)
            self.received.put(data)
            
                