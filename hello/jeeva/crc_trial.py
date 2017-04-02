'''
Created on Mar 19, 2017

@author: jee11
'''
import PyCRC.CRC16
from PyCRC.CRCCCITT import CRCCCITT

my_crc=CRCCCITT()
print(my_crc.calculate("00000001"))
print(my_crc.calculate("i love you harika, but i wanna fuck you! Woah! how much ever text i give, this shit is giving only 5 digit"))


if __name__ == '__main__':
    pass