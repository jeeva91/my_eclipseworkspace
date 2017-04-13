'''
Created on Apr 1, 2017

@author: jee11
'''


from threading import Thread
from threading import Lock
from queue import Queue
from asyncio.tasks import sleep
import time

class Producer_Thread(Thread):
    '''
    classdocs
    '''


    def __init__(self,queue,lock=Lock()):
        '''
        Constructor
        '''
        self.pqueue=queue
        self.lock=lock
        print("inside producer constructor")
        
        Thread.__init__(self)
        
    def run(self):
        '''
        '''
        self.produce()
        
                
    
    
    def produce(self):
        pass
        counter=0
        while(True):
            self.lock.acquire()
            print("putting {} in queue".format(counter))
            self.pqueue.put(counter)
            counter=counter+1
            self.lock.release()
            time.sleep(1)
    