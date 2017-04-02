'''
Created on Mar 29, 2017

@author: jee11
'''

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



if __name__ == '__main__':
    pass