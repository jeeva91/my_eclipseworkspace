'''
Created on Apr 13, 2017

@author: Quest10
'''
from tkinter import *
from QuEST.UI import UIWidgets

class SettingsFrame(Frame):
    def __init__(self,master,all_data):
        Frame.__init__(self, master)
        self.all_data=all_data
        self.TDC_part=Label(self,text="TDC Setting",width=25)
        self.port_input=UIWidgets.InputFrame(self,label_text="Port No")
        print("port_type")
        print(type(self.port_input))
        self.baud_input=UIWidgets.InputFrame(self,label_text="Baud rate")
        self.change_button=UIWidgets.ChangeButton(self,self.all_data)
        self.start_button=UIWidgets.StartButton(self,master.console,self.all_data)
        self.stop_button=UIWidgets.StopButton(self,serial_reader_thread="null")
        
        self.TDC_part.grid(row=0, column=0, sticky=W)
        self.port_input.grid(row=1,column=0, sticky=W)
        self.baud_input.grid(row=2,column=0,sticky=W)
        self.change_button.grid(row=3,column=0,sticky=W)
        self.start_button.grid(row=4,column=0,sticky=W)
        self.stop_button.grid(row=5,column=0,sticky=W)
        
        
        comm_part=Label(self,text="Communication Setting",width=25).grid(row=0,column=1,sticky=W)
        IP_input=UIWidgets.InputFrame(self,label_text="IP:").grid(row=1,column=1,sticky=W)
        if_server=UIWidgets.CheckBoxFrame(self,label_text="Server").grid(row=2,column=1,sticky=W)
        conect=UIWidgets.ConnectButton(self,mytcpsocket="null").grid(row=3,column=1,sticky=W)
        disconnect=UIWidgets.DisconnectButton(self,mytcpsocket="null").grid(row=4,column=1,sticky=W)
        
        start_sending=UIWidgets.StartSendingButton(self,mytcpsocket="null").grid(row=5,column=1,sticky=W)
        
class AllConsole(Frame):
    def __init__(self,master,all_data):
        Frame.__init__(self,master)
        self.all_data=all_data
        self.micro_time=UIWidgets.ConsoleFrame(self,time_queue="null",console_name="micro time")
        self.good_utime=UIWidgets.ConsoleFrame(self,time_queue="null",console_name="good micro time")
        self.micro_time.grid(row=0,column=0,sticky=W)
        self.good_utime.grid(row=0,column=1,sticky=W)