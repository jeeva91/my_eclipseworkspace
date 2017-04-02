'''
Created on Mar 15, 2017

@author: jee11
'''
from tkinter import *
root = Tk()
T = Text(root, height=2, width=30)
T.pack()
T.insert(END, "Just a text Widget\nin two lines\n")
def insertotext():
    T.insert(END,"i love harika")
    T.see(END)
    T.after(500,insertotext)
T.after(50, insertotext)
root.mainloop()

