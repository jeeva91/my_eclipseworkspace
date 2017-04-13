'''
Created on Apr 1, 2017

@author: jee11
'''

from threading import Thread
from queue import Queue
from threading import Lock

class Consumer_Thread(Thread):
    '''
    classdocs
    '''


    def __init__(self,queue,lock=Lock()):
        '''
        Constructor
        '''
        self.cqueue=queue
        self.lock=Lock()
        print("inside Consumer constructor")

        Thread.__init__(self)
        
    def run(self):
        '''
        '''
        self.consume()
        
    
    
    def consume(self):
        while(True):
            self.lock.acquire()
            print("inside consumer")
            if(~self.cqueue.empty()):
                data=self.cqueue.get()
                print("got {} from the queue".format(data))
            self.lock.release()
        
        
                
        
    
    