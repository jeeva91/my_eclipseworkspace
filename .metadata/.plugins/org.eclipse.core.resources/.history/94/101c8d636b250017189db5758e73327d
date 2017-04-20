'''
Created on Apr 13, 2017

@author: Quest10
'''
from tkinter import *
from QuEST.UI import UIWidgets

class SettingsFrame(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        TDC_part=Label(self,text="TDC Setting",width=25).grid(row=0, column=0, sticky=W)
        port_input=UIWidgets.InputFrame(self,label_text="Port No").grid(row=1,column=0, sticky=W)
        baud_input=UIWidgets.InputFrame(self,label_text="Baud rate").grid(row=2,column=0,sticky=W)
        change_button=UIWidgets.ChangeButton(self,serial_reader="null").grid(row=3,column=0,sticky=W)
        start_button=UIWidgets.StartButton(self,serial_reader_thread="null").grid(row=4,column=0,sticky=W)
        stop_button=UIWidgets.StopButton(self,serial_reader_thread="null").grid(row=5,column=0,sticky=W)
        
        
        comm_part=Label(self,text="Communication Setting",width=25).grid(row=0,column=1,sticky=W)
        IP_input=UIWidgets.InputFrame(self,label_text="IP:").grid(row=1,column=1,sticky=W)
        if_server=UIWidgets.CheckBoxFrame(self,label_text="Server").grid(row=2,column=1,sticky=W)
        conect=UIWidgets.ConnectButton(self,mytcpsocket="null").grid(row=3,column=1,sticky=W)
        disconnect=UIWidgets.DisconnectButton(self,mytcpsocket="null").grid(row=4,column=1,sticky=W)
        
        start_sending=UIWidgets.StartSendingButton(self,mytcpsocket="null").grid(row=5,column=1,sticky=W)
        
class AllConsole(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        micro_time=UIWidgets.ConsoleFrame(self,time_queue="null",console_name="micro time").grid(row=0,column=0,sticky=W)
        good_utime=UIWidgets.ConsoleFrame(self,time_queue="null",console_name="good micro time").grid(row=0,column=1,sticky=W)
        