'''
Created on Mar 8, 2017

@author: jee11
'''
import serial
#import unicodedata
myserial = serial.Serial()
myserial.baudrate=38400
myserial.port='COM8'
print("cheking if the connection is open")
print(myserial.isOpen())
print("trying to open port")
myserial.open()
print("cheking if the connection is open")
print(myserial.isOpen())
print(myserial)

if __name__ == '__main__':
    pass
    while(1):   
        data =myserial.read(1)     
        #print(myserial.read(1))  #read byte
        #data=myserial.read())
        print(data)
        #print(type(data))
  
