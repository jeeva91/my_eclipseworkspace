'''
Created on Mar 15, 2017

@author: jee11
'''
from tkinter import *
#from ScrolledText import *

#text_pad = scrolledtext(home, width=100, height=70).pack()
#scrolledtext()
if __name__ == '__main__':
    pass
    home=Tk()
    home.title("QuEST TDC")
    i=1
    welcome_label=Label(home,text="Welcome to QuEST TDC").pack()
    text_pad=Text(home,width=100,height=50)
    text_pad.pack()
    text_pad.insert(END,"fuck")
    text_pad.insert(END,"fuck")
    home.mainloop()
    text_pad.insert(END, "Dog")
    #for iter in range(1,100):
    
      #home.mainloop()
      