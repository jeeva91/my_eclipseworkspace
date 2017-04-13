'''
Created on Apr 1, 2017

@author: jee11
'''
from threading import Thread
from queue import Queue
from jeeva.hello import Producer_Thread
from jeeva.hello import Consumer_Thread

my_queue=Queue(0)

producer=Producer_Thread.Producer_Thread(my_queue)
consumer=Consumer_Thread.Consumer_Thread(my_queue)

print("starting producer")
producer.start()

print("Starting consumer")
consumer.start()






if __name__ == '__main__':
    pass