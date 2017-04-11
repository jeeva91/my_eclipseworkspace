'''
Created on Apr 11, 2017

@author: Quest01
'''
import datetime
import re

datetime.datetime.now()
print(datetime.datetime.now())
my_current_time=datetime.datetime.now()
print(my_current_time)
print(type(my_current_time))

mytime_string=str(my_current_time)
print(mytime_string)
print(type(mytime_string))

mytime_string=re.sub(r"\s+",'__',mytime_string)
print(mytime_string)
if __name__ == '__main__':
    pass