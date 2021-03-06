'''
Created on Apr 1, 2017

to test My_TCP, Sender_Thread, Receiver_thread

@author: jee11
'''
from queue import Queue
import socket

#import hello.jeeva.hello.My_TCP.My_TCP
#import jeeva.hello.Receiver_Thread.Receiver_Thread
#import jeeva.hello.Sender_Thread.Sender_Thread

from jeeva.hello import My_TCP
from threading import Thread
from asyncio.tasks import sleep
from jeeva.hello import Sender_Thread
from jeeva.hello import Receiver_Thread
from jeeva.hello import Send_Processor
from jeeva.hello import Received_Processor

server_send=Queue(0)
server_receive=Queue(0)
client_send=Queue(0)
client_receive=Queue(0)
ip="127.0.0.1"
#kwargs={'ip':"127.0.0.1" , 'port': 5005, 'con_type': "server"}
#server_thread=Thread(target=My_TCP.My_TCP(), **kwargs)
server_socket=My_TCP.My_TCP("127.0.0.1",5005,"server")
client_socket=My_TCP.My_TCP("127.0.0.1",5005,"client")

server_sender=Sender_Thread.Sender_Thread(server_send,server_socket.conn)
server_receiver=Receiver_Thread.Receiver_Thread(server_receive,server_socket.conn)

client_sender=Sender_Thread.Sender_Thread(client_send,client_socket.my_socket)
client_receiver=Receiver_Thread.Receiver_Thread(client_receive,client_socket.my_socket)

server_send_processor= Send_Processor.Send_Processor(server_send)
server_receive_processor=Received_Processor.Received_Processor(server_receive,con_type="server")

client_send_processor=Send_Processor.Send_Processor(client_send)
client_receive_processor=Received_Processor.Received_Processor(client_receive,con_type="client")

server_sender.start()
server_receiver.start()

client_sender.start()
client_receiver.start()

server_send_processor.start()
server_receive_processor.start()


client_send_processor.start()
client_receive_processor.start()





        






