'''
Created on Apr 14, 2017

@author: jee11
'''

class MyClass(object):
    '''
    classdocs
    '''
    #variable 

    def __init__(self):
        '''
        Constructor
        '''
        global variable=1
        print("before calling the obj_class")
        print(variable)
        obj=ObjectClass(variable)
        print("after calling the obj_class")
        print(variable)
        

class ObjectClass():
    
    def __init__(self, variable):
        self.variable = variable
        self.method()
        
    def method(self):
        self.varialbe=2
        
        
my_class=MyClass()

