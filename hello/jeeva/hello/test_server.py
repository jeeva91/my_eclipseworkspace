'''
Created on Apr 2, 2017

@author: jee11
'''
from queue import Queue
import socket
from jeeva.hello import My_TCP
from threading import Thread
from asyncio.tasks import sleep
from jeeva.hello import Sender_Thread
from jeeva.hello import Receiver_Thread
from jeeva.hello import Send_Processor
from jeeva.hello import Received_Processor

server_send=Queue(0)
server_receive=Queue(0)

server_socket=My_TCP.My_TCP("127.0.0.1",5007,"client")