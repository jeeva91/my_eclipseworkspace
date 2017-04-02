'''
Created on Apr 1, 2017

@author: jee11
'''

from threading import Thread
from queue import Queue

class Consumer_Thread(Thread):
    '''
    classdocs
    '''


    def __init__(self,queue):
        '''
        Constructor
        '''
        self.cqueue=queue
        print("inside Consumer constructor")

        Thread.__init__(self)
        
    def run(self):
        '''
        '''
        self.consume()
        
    
    
    def consume(self):
        while(True):
            print("inside consumer")
            if(~self.cqueue.empty()):
                data=self.cqueue.get()
                print("got {} from the queue".format(data))
        
        
                
        
    
    