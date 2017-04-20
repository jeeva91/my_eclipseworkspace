'''
Created on Apr 15, 2017

@author: jee11
'''

class MyDataClass(object):
    '''
    classdocs
    '''
    _my_integer=1

    def __init__(self):
        '''
        Constructor
        '''
    @property
    def my_integer(self):
        return(self._my_integer)
    
    @my_integer.setter
    def my_integer(self,variable):
        self._my_integer=variable
        
    
    
mydataclass1=MyDataClass()
mydataclass2=MyDataClass()

print("Object one integer is:")
print(mydataclass1.my_integer)


print("object 2 integer is ")
print(mydataclass2.my_integer)
print("changing the static integer to 2 from the object one")

mydataclass1.my_integer=2

print(" chekcing if the value is changed from object 2")

print(mydataclass2.my_integer)

print("Checking the value from the class:"+ str(MyDataClass.my_integer))

print(MyDataClass.my_integer)


        