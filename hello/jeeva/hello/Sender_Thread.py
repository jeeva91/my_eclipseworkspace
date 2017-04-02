'''
Created on Apr 1, 2017

@author: jee11
'''
from threading import Thread
from queue import Queue
from _overlapped import NULL
from _socket import socket
class Sender_Thread(Thread):
    '''
    classdocs
    '''
    

    def __init__(self,tosend=Queue(0),send_socket=socket):
        '''
        Constructor
        '''
        self.sender_switch="True"
        self.send_socket=send_socket
        self.tosend=tosend
        Thread.__init__(self)
        
    def run(self):
        pass
        self.send()
    
    def send(self):    
        while(self.sender_switch=="True"):
            pass
            if (~self.tosend.empty()):
                self.send_socket.send(str(self.tosend.get())
                
                
            
        
        
        
        