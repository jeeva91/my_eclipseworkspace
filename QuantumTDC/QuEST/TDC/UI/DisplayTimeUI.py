'''
Created on Mar 15, 2017

@author: jee11
'''
from tkinter import *
from QuEST.TDC.UI import UIWidgets

class DisplayTimeUI(Tk):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        Tk.__init__(self)
        port_label=UIWidgets.LabelFrame(self,label_text="Port No").grid(row=0,column=0)
        if_server=UIWidgets.CheckBoxFrame(self,label_text="Server").grid(row=1,column=0,sticky=W)
        
my_display=DisplayTimeUI()
my_display.mainloop(0)