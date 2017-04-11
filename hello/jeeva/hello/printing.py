'''
Created on Mar 29, 2017

@author: jee11
'''
import re

data="dog "+"\n"+"j"+"\n"+"fuck"
print(data)
n=data.count("\n")
print(n)
n=data.count(" ")
print(n)
parti=data.partition("\n")
first=parti[0]
next=parti[2]
print(parti)
print(first)
print(next)


my_string="how are you doing?"
print("my_string with space")
print(my_string)
my_string=re.sub(r"\s+",'_',my_string)
print("my_string space replaced with _")
print(my_string)


if __name__ == '__main__':
    pass