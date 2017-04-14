'''
Created on Apr 1, 2017

@author: jee11
'''
from threading import Thread
from threading import Lock
from queue import Queue
from _overlapped import NULL
from _socket import socket
import time
class Receiver_Thread(Thread):
    '''
    classdocs
    '''
    

    def __init__(self,received=Queue(0),rcv_socket=socket,lock=Lock()):
        '''
        Constructor
        '''
        self.receiver_switch="True"
        self.received=received
        self.rcv_socket=rcv_socket
        self.lock=lock
        Thread.__init__(self)
        
    def run(self):
        pass
        self.receive()
    
    def receive(self):
        while(self.receiver_switch=="True"):
            pass
            #self.lock.acquire()
            data=self.rcv_socket.recv(1024)
            self.received.put(data)
            #self.lock.release()
            time.sleep(0.25)
            
                