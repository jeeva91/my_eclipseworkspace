'''
Created on Apr 1, 2017

@author: jee11
'''
from threading import Thread
from threading import Lock
from queue import Queue
from asyncio.tasks import sleep
import time

class Send_Processor(Thread):
    
    def __init__(self,send_Q=Queue(0),lock=Lock()):
        self.send_Q=send_Q
        self.lock=lock
        Thread.__init__(self)
    
    
    def run(self,):
        pass
        self.send_process()
        
        
    def send_process(self):    
        counter=1
        while(True):
            self.lock.acquire()
            self.send_Q.put(counter)
            counter=counter+1
            time.sleep(0.5)
            self.lock.release()
            
    