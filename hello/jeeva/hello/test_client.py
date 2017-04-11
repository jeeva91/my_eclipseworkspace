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


client_send=Queue(0)
send_lock=Lock()
client_receive=Queue(0)
receive_lock=Lock()

client_socket=My_TCP.My_TCP("192.168.1.162",5005,"client")

client_sender=Sender_Thread.Sender_Thread(client_send,client_socket.my_socket,lock=send_lock)
client_receiver=Receiver_Thread.Receiver_Thread(client_receive,client_socket.my_socket,lock=receive_lock)


client_send_processor=Send_Processor.Send_Processor(client_send,lock=send_lock)
client_receive_processor=Received_Processor.Received_Processor(client_receive,con_type="client",lock=receive_lock)

client_sender.start()
client_receiver.start()

client_send_processor.start()
client_receive_processor.start()
