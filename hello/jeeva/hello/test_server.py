'''
Created on Apr 2, 2017

@author: jee11
'''
from queue import Queue
import socket
from jeeva.hello import My_TCP
from threading import Thread
from threading import Lock
from asyncio.tasks import sleep
from jeeva.hello import Sender_Thread
from jeeva.hello import Receiver_Thread
from jeeva.hello import Send_Processor
from jeeva.hello import Received_Processor

server_send=Queue(0)
send_lock=Lock()
server_receive=Queue(0)
receive_lock=Lock()
server_socket=My_TCP.My_TCP("155.246.202.169",5005,"server")

server_sender=Sender_Thread.Sender_Thread(server_send,server_socket.conn,lock=send_lock)
server_receiver=Receiver_Thread.Receiver_Thread(server_receive,server_socket.conn,lock=receive_lock)

server_send_processor= Send_Processor.Send_Processor(server_send,lock=send_lock)
server_receive_processor=Received_Processor.Received_Processor(server_receive,con_type="server",lock=receive_lock)

server_sender.start()
server_receiver.start()

server_send_processor.start()
server_receive_processor.start()
