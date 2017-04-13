'''
Created on Apr 13, 2017

@author: jee11
'''
from tkinter import Frame, IntVar
from tkinter import Label
from tkinter import Entry
from tkinter import *
class InputFrame(Frame):
    def __init__(self,master,label_text="label"):
        Frame.__init__(self, master,width=350,height=70)
        print(self.winfo_height())
        print(self.winfo_width())
        self.label=Label(self,text=label_text,width=12).pack(side=LEFT)
        self.entry=Entry(self,width=10).pack(side=RIGHT)
    def get_data(self):
        return self.entry.get()
    
class CheckBoxFrame(Frame):
    def __init__(self,master,label_text="server"):
        Frame.__init__(self,master,width=350,height=70)
        #self.label=Label(self,text=label_text).pack(side=LEFT)
        self.checkbox=Checkbutton(self,text=label_text).pack()
        
class ChangeButton(Button):        
    def __init__(self,master,serial_reader):
        Button.__init__(self,master,text="Change",command=self.change,width=12)
        self.serial_reader=serial_reader
    def change(self):
        pass
        print("Changed clicked")
        
class StartButton(Button):        
    def __init__(self,master,serial_reader_thread):
        Button.__init__(self,master,text="Start",command=self.start,width=12)
        self.serial_reader=serial_reader_thread
    def start(self):
        pass
        print("Starting to read from TDC")
        
class StopButton(Button):        
    def __init__(self,master,serial_reader_thread):
        Button.__init__(self,master,text="Stop",command=self.stop,width=12)
        self.serial_reader=serial_reader_thread
    def stop(self):
        pass
        print("Stopping to read from TDC")
        
class ConnectButton(Button):        
    def __init__(self,master,mytcpsocket):
        Button.__init__(self,master,text="Connect",command=self.connect,width=12)
        self.mytcpsocket=mytcpsocket
    def connect(self):
        pass
        print("Connecting to the server/client")
        
class DisconnectButton(Button):        
    def __init__(self,master,mytcpsocket):
        Button.__init__(self,master,text="Disconnect",command=self.disconnect,width=12)
        self.mytcpsocket=mytcpsocket
    def disconnect(self):
        pass
        print("disConnecting to the server/client")
        
class StartSendingButton(Button):        
    def __init__(self,master,mytcpsocket):
        Button.__init__(self,master,text="Communicate",command=self.send,width=12)
        self.mytcpsocket=mytcpsocket
    def send(self):
        pass
        print("Communicating with the other lab")        
        