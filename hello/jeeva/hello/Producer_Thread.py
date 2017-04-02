'''
Created on Apr 1, 2017

@author: jee11
'''


from threading import Thread
from queue import Queue
from asyncio.tasks import sleep
import time

class Producer_Thread(Thread):
    '''
    classdocs
    '''


    def __init__(self,queue):
        '''
        Constructor
        '''
        self.pqueue=queue
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
            print("putting {} in queue".format(counter))
            self.pqueue.put(counter)
            counter=counter+1
            time.sleep(1)
    