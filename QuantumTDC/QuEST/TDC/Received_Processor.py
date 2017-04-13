'''
Created on Apr 1, 2017

@author: jee11
'''

from threading import Thread
from queue import Queue
from threading import Lock
import time

class Received_Processor(Thread):
    
    def __init__(self, received_Q=Queue(0),con_type="client",lock=Lock()):
        self.received_Q=received_Q
        self.con_type=con_type
        self.lock=lock
        Thread.__init__(self)
        
    
    
    def run(self):
        pass
        self.receive_process()
        
        
    def receive_process(self):    
        while(True):
            #self.lock.acquire()
            if(~self.received_Q.empty()):
                data=self.received_Q.get()
                print("from{} data{}".format(self.con_type,data))
            #self.lock.release()
            time.sleep(0.25)