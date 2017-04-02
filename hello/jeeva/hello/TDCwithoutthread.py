'''
Created on Mar 16, 2017

@author: jee11
'''
from tkinter import *
from QuEST.TDC.SerialReader import SerialReader

root=Tk()
root.title("QuEST TDC")
text_pad=Text(root, width=100, height=50)
text_pad.pack()
text_pad.insert(END,"hI")
tdc_serial=SerialReader(port='COM1',baudrate=38400)
tdc_serial.start_TDC()

def print_to_pad():
    data=tdc_serial.read(1)
    text_pad.insert(END,data)
    text_pad.after(50,print_to_pad)
text_pad.after(1,print_to_pad)
root.mainloop()
    