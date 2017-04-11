'''
Created on Apr 11, 2017

@author: Quest01
'''
import os

print(" this is the current directory")
print(os.getcwd())
os.chdir(r'C:\Users\Quest01\Documents')
print(" this is the current directory")
print(os.getcwd())
datafile=open("testing_append.txt", "a+")
print(os.path.abspath("testing_append.txt"))

print(" this is the current directory")
print(os.getcwd())

for i in range(0,10):
    pass
    data ="this is line number"+str(i)
    data.encode('utf-8')
    datafile.write(data)
    datafile.write("\n")
 


if __name__ == '__main__':
    pass