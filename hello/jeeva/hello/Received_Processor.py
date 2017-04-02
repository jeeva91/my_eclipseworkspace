'''
Created on Apr 1, 2017

@author: jee11
'''

from threading import Thread
from queue import Queue

class Received_Processor(Thread):
    
    def __init__(self, received_Q=Queue(0),con_type="client"):
        self.received_Q=received_Q
        self.con_type=con_type
        
    
    
    def run(self):
        pass
        self.receive_process()
        
        
    def receive_process(self):    
        while(True):
            if(~self.received_Q.empty()):
                data=self.received_Q.get()
                print("from{} data{}".format(self.con_type,data))